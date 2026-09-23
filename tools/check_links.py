#!/usr/bin/env python3
"""校验仓库内的相对链接与目录锚点。用法：python3 tools/check_links.py"""
import collections
import glob
import os
import re
import subprocess
import sys
import unicodedata
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = ('_archive/', '.qoder/', 'node_modules/')
LINK = re.compile(r'\]\((?!https?:|mailto:|#)([^)#]+)(#[^)]*)?\)')
ANCHOR = re.compile(r'\]\(#([^)]+)\)')
HEAD = re.compile(r'^#{2,4} (.+)')
TAG = re.compile(r'<[^>]+>')
IMG = re.compile(r'!\[([^\]]*)\]\([^)]*\)')
MDLINK = re.compile(r'\[([^\]]*)\]\([^)]*\)')
CODE = re.compile(r'`+([^`]*)`+')


def slug(heading):
    """复刻 GitHub 的标题锚点规则。

    关键：GitHub 的锚点取自标题**渲染后的文字**，因此 markdown 链接的 URL 必须
    先丢弃、只保留链接文字（`[Anthropic](https://x.com)` → `anthropic`），
    `²` 等非十进制数字与 emoji、`&`、`$` 一样被剔除。
    """
    text = TAG.sub('', heading)
    text = IMG.sub(r'\1', text)
    text = MDLINK.sub(r'\1', text)
    text = CODE.sub(r'\1', text)
    out = []
    for ch in text.lower():
        if ch in ' \t':
            out.append('-')
        elif unicodedata.category(ch)[0] in 'LM' or unicodedata.category(ch) == 'Nd' or ch in '-_':
            out.append(ch)
    return ''.join(out)


def headings_of(text):
    seen, known = collections.Counter(), set()
    for line in text.split('\n'):
        m = HEAD.match(line)
        if not m:
            continue
        s = slug(m.group(1))
        known.add(s)
        seen[s] += 1
        if seen[s] > 1:
            known.add(f'{s}-{seen[s] - 1}')
    return known


def main():
    slug_errs = _slug_selftest()
    files = [
        f for f in glob.glob('**/*.md', root_dir=ROOT, recursive=True)
        if not f.startswith(SKIP_DIRS)
    ]
    errors = list(slug_errs)
    tracked = tracked_paths()
    for rel in sorted(files):
        path = os.path.join(ROOT, rel)
        with open(path, encoding='utf-8') as fh:
            text = fh.read()
        anchors = headings_of(text) if rel == 'README.md' else None
        for m in LINK.finditer(text):
            target = urllib.parse.unquote(m.group(1))
            if not target:
                continue
            resolved = os.path.join(ROOT, os.path.dirname(rel), target)
            if not exists_exact(resolved):
                errors.append(f'{rel}:{_line(text, m)} 死链 -> {target}')
            elif tracked is not None:
                idx = os.path.normpath(os.path.join(os.path.dirname(rel), target))
                if not in_index(tracked, idx):
                    errors.append(
                        f'{rel}:{_line(text, m)} 链接目标未入库或大小写与索引不符'
                        f'（GitHub 上会 404）-> {target}')
        if anchors is not None:
            for m in ANCHOR.finditer(text):
                if m.group(1) not in anchors:
                    errors.append(f'{rel}:{_line(text, m)} 锚点未命中 -> #{m.group(1)}')

    if errors:
        print('\n'.join(errors))
        print(f'\n{len(errors)} 处问题 / 扫描 {len(files)} 个文件')
        return 1
    print(f'链接与锚点检查通过（{len(files)} 个文件）')
    return 0


def exists_exact(path):
    """逐级严格比对目录名，绕过 macOS/Windows 的大小写不敏感文件系统。"""
    cur = ROOT
    for part in os.path.relpath(path, ROOT).split(os.sep):
        if part in ('', '.'):
            continue
        if part == '..':
            cur = os.path.dirname(cur)
            continue
        try:
            names = os.listdir(cur)
        except OSError:
            return False
        if part not in names:
            return False
        cur = os.path.join(cur, part)
    return True


def tracked_paths():
    """git 索引里的确切路径集合，非 git 环境返回 None。

    GitHub 渲染的是**提交进去的树**，不是本地工作目录。本次要防的正是「本地
    `gtm/`、正文链 `./gtm/`、但索引里实际入库为 `GTM/`」——os.path.exists 在
    macOS 上一路绿灯，线上却是 404。只有拿索引比对才抓得住。
    """
    try:
        out = subprocess.run(['git', 'ls-files', '-z'], cwd=ROOT,
                             capture_output=True, text=True, check=True)
    except Exception:
        return None
    return {p for p in out.stdout.split('\0') if p}


def in_index(tracked, rel):
    return rel in tracked or any(t.startswith(rel + '/') for t in tracked)


def _line(text, match):
    return text[:match.start()].count('\n') + 1


# 期望值取自 GitHub REST `/repos/…/readme`（Accept: application/vnd.github.html）
# 渲染出的真实 heading id，不是本地约定。若有人改动 slug() 使其偏离 GitHub，
# 这里会立刻失败——避免「生成端与校验端共享同一个错误算法」造成的假绿灯。
SLUG_TRUTH = [
    ('2. [Anthropic](https://anthropic.com) — 🌟 $965B', '2-anthropic---965b'),
    ('4. [Palantir Technologies](https://palantir.com) — $400B+（已上市）',
     '4-palantir-technologies--400b已上市'),
    ('11. [自变量机器人 / X-Square Robot](https://xsquare.com) — 🔥 RMB 100 亿+',
     '11-自变量机器人--x-square-robot---rmb-100-亿'),
    ('12. [智平方 / AI² Robotics](https://ai2robotics.com) — 🔥 RMB 100 亿+（深圳首家百亿具身独角兽）',
     '12-智平方--ai-robotics---rmb-100-亿深圳首家百亿具身独角兽'),
    ('14. [Enflame / 燧原科技](https://enflame-tech.com) — ~$20B+',
     '14-enflame--燧原科技--20b'),
    ('[Bridge (Stripe 子公司)](https://bridge.xyz) — 被 Stripe 收购 $1.1B',
     'bridge-stripe-子公司--被-stripe-收购-11b'),
    ('[D-Wave Systems](https://dwavesys.com) — 已上市', 'd-wave-systems--已上市'),
    ('[Wiz](https://wiz.io) — $32B → 被收购 $42B', 'wiz--32b--被收购-42b'),
    ('🏆 顶级独角兽 & 超级独角兽', '-顶级独角兽--超级独角兽'),
    ('⚡ 估值 / 市值速查表', '-估值--市值速查表'),
]


def _slug_selftest():
    return [f'锚点算法偏离 GitHub: {raw!r} -> {got!r}（应为 {want!r}）'
            for raw, want in SLUG_TRUTH if (got := slug(raw)) != want]


if __name__ == '__main__':
    sys.exit(main())
