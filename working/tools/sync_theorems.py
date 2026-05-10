import re
import os
import json
from pathlib import Path

tex_root = Path(r"d:/ZJU/Study Materials/algebra 2/summary/Linear-Algebra-Left-Undone/讲义")
md_path = Path(r"d:/ZJU/Study Materials/algebra 2/summary/LALU_full_theorems/LALU_full_theorems.md")
report_path = Path(r"d:/ZJU/Study Materials/algebra 2/summary/LALU_missing_report.md")

env_re = re.compile(r"\\begin\{(definition|theorem|lemma)\}(?:\{([^}]*)\})?(?:\{([^}]*)\})?", re.MULTILINE)
end_re_template = r"\\end\{%s\}"

md_text = md_path.read_text(encoding='utf-8')

missing = []

for tex_file in tex_root.rglob('*.tex'):
    text = tex_file.read_text(encoding='utf-8')
    for m in env_re.finditer(text):
        env = m.group(1)
        title = (m.group(2) or '').strip()
        # if no explicit title, try to extract a short preview of the body
        start = m.end()
        end_pat = re.compile(end_re_template % env)
        end_m = end_pat.search(text, start)
        body = ''
        if end_m:
            body = text[start:end_m.start()].strip()
        preview = ''
        if title:
            key = title
        else:
            preview = ' '.join(line.strip() for line in body.splitlines() if line.strip())[:120]
            key = preview
        # basic presence check in md
        if key and key in md_text:
            continue
        missing.append({
            'file': str(tex_file.relative_to(tex_root.parent)),
            'env': env,
            'title': title,
            'preview': preview,
            'body_snippet': preview,
        })

# group by chapter (approx by source file path)
by_file = {}
for item in missing:
    by_file.setdefault(item['file'], []).append(item)

# write report
lines = ["# 缺失条目报告\n", "生成说明：列出在 TeX 中存在但在 LALU_full_theorems.md 中未发现的定理/定义/引理。\n\n"]
for f, items in sorted(by_file.items()):
    lines.append(f"## {f}\n")
    for it in items:
        env = it['env']
        title = it['title'] if it['title'] else '(无题，使用内容预览)'
        lines.append(f"- **{env}**: {title}\n")
        if it['body_snippet']:
            lines.append(f"  - 预览：{it['body_snippet']}\n")
        # suggested md snippet
        md_env = '定义' if env=='definition' else ('引理' if env=='lemma' else '定理')
        md_snip = f"**{md_env} (待编号) ({title})**  （此处从 TeX 提取的内容需人工校订并转换为 KaTeX）\n"
        lines.append(f"  - 建议插入：\n\n    {md_snip}\n")
    lines.append('\n')

report_path.write_text('\n'.join(lines), encoding='utf-8')
print(f"报告已写入: {report_path}")
