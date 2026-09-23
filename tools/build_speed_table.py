#!/usr/bin/env python3
"""从 README 正文派生「⚡ 估值 / 市值速查表」，就地重建该章节。

设计纪律
--------
1. 单元格只能是条目标题里已有文字的**逐字副本**；脚本唯一计算的东西是排序键
   （数字降序）与 GitHub 锚点。不新增、不改写任何事实或数字。
2. 锚点算法从 tools/check_links.py 导入，与本仓库校验器共用同一份实现，
   避免「生成端与校验端各自演化」造成的假通过。
3. 幂等：只要正文标题不变，重复运行不产生 diff。

用法：python3 tools/build_speed_table.py [--check]
      --check  只报告差异，不写文件（供 CI 使用）。
"""
import collections
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_links import slug  # noqa: E402  与校验器共用锚点算法

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(ROOT, 'README.md')

HEADING = '## ⚡ 估值 / 市值速查表'
THRESHOLD = 10.0          # 单位：$B
HEAD = re.compile(r'^(#{2,4}) (.+)$')
ENTRY = re.compile(r'^(?:\d+\.\s*)?\[([^\]]+)\]\((?!#)[^)]+\)(.*?)\s+—\s+(.+)$')
AMOUNT = re.compile(r'\$\s*([\d.]+)\s*([TB])\b')
TRACK = re.compile(r'^\s*-\s*\*\*赛道\*\*：(.+)')
DECOR = re.compile(r'^[^\w一-鿿A-Za-z]+')


def clean(heading):
    """去掉 emoji / 符号等装饰性前缀，得到可读的赛道或区域名。"""
    return DECOR.sub('', heading).strip()


def amount(tail):
    m = AMOUNT.search(tail)
    return None if not m else float(m.group(1)) * (1000 if m.group(2) == 'T' else 1)


def collect(lines):
    """扫描条目标题，返回 {去重键: 行数据}。"""
    h2 = h3 = ''
    rows = {}
    for i, line in enumerate(lines):
        hm = HEAD.match(line)
        if not hm:
            continue
        level, text = hm.group(1), hm.group(2)

        if level == '##':
            h2, h3 = clean(text), ''
            continue
        if level == '###' and not ENTRY.match(text):
            h3 = clean(text)
            continue
        em = ENTRY.match(text)
        if not em:
            continue
        name, note, tail = (em.group(g).strip() for g in (1, 2, 3))
        if len(note) > 40 or '[' in note:      # 链接后的括号注记过长 → 非标准条目
            continue
        val = amount(tail)
        if val is None or val < THRESHOLD:
            continue

        track = (h3 or h2) if level == '####' else h2
        for j in range(i + 1, min(i + 8, len(lines))):
            if HEAD.match(lines[j]):
                break
            tm = TRACK.match(lines[j])
            if tm:
                track = clean(tm.group(1))
                break

        key = re.sub(r'[^a-z0-9]', '', name.lower()) or name
        keep = rows.get(key)
        if keep is None or val > keep['val'] or (
                val == keep['val'] and keep['level'] == '###' and level == '####'):
            rows[key] = dict(name=name, tail=tail, val=val, track=track,
                             anc=slug(text), level=level)
    return list(rows.values())


def render(rows):
    rows = sorted(rows, key=lambda r: (-r['val'], r['name']))
    return [
        HEADING,
        '',
        f'> 收录正文中 **估值 / 市值 ≥ $10B** 的全部 {len(rows)} 家条目，按数字降序；'
        '点击公司名直达条目正文。',
        '>',
        '> **口径**：数字逐字照抄条目标题——私营公司为最近一轮融资估值，'
        '标 `已上市` 者为市值、`~` 为近似值，'
        '`（并购对价）`为收购交易金额、`（合并交易估值）`为并购中该方的计价、'
        '`（交易隐含）`为按持股比例倒推的整体定价、'
        '`（估）`/`（2022 高点）`/`（融资中）`/`（洽谈中）` 等为原文限定。'
        '各类数字不可直接比较，详见[数据口径说明](#数据口径说明)。',
        '',
        '| # | 公司 | 估值 / 市值 | 赛道 / 区域 |',
        '| --- | --- | --- | --- |',
        *[f"| {n} | [{r['name']}](#{r['anc']}) | **{r['tail']}** | {r['track']} |"
          for n, r in enumerate(rows, 1)],
        '',
        '<sub>💡 本表由 `python3 tools/build_speed_table.py` 从正文标题派生，'
        '不重复轮次与细节；完整数据以条目正文为准。'
        '新增条目只要在标题写 `— $XB`，重跑脚本即可复算本表。</sub>',
    ]


def main():
    check = '--check' in sys.argv
    lines = open(README, encoding='utf-8').read().split('\n')
    try:
        start = lines.index(HEADING)
    except ValueError:
        print(f'未找到章节标题：{HEADING}')
        return 1
    end = next(i for i in range(start, len(lines)) if lines[i].startswith('<sub>💡 本表'))
    old = lines[start:end + 1]
    new = render(collect(lines))
    toc_anchor = '- [⚡ 估值 / 市值速查表](#' + slug(HEADING[3:]) + ')'
    toc_ok = any(l.rstrip().startswith(toc_anchor) for l in lines)

    if old == new:
        print(f'速查表已是最新（{len(new) - 10} 行）' + ('' if toc_ok else '；⚠ 目录锚点未命中'))
        return 0 if toc_ok else 1
    if check:
        for a, b in zip(old, new):
            if a != b:
                print(f'差异\n  现: {a}\n  应: {b}')
        print(f'速查表与正文不一致（{len(old) - 10} 行 vs {len(new) - 10} 行）→ 请运行 '
              'python3 tools/build_speed_table.py')
        return 1
    lines[start:end + 1] = new
    open(README, 'w', encoding='utf-8').write('\n'.join(lines))
    print(f'已重建速查表：{len(new) - 10} 行')
    return 0


if __name__ == '__main__':
    sys.exit(main())
