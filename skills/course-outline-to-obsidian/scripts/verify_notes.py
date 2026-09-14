#!/usr/bin/env python3
"""结构化笔记库（Obsidian vault）校验器（通用）。

用法：
    python verify_notes.py <库根目录> [选项]

选项：
    --expect-notes N        期望的笔记总数（只统计笔记，不统计索引/模板）
    --notes-glob PREFIX     视为"笔记"的文件前缀（默认自动识别：以 0/1/2/3/4/5/6/7/8/9 开头的章节目录）
    --exclude a,b,c         额外排除的目录名（默认已排除 .obsidian / .git / 附件 / 模板 等）
    --sections "甲,乙,丙"    要求每篇笔记都包含的小标题关键词（可只给关键词，如 "第一性原理"）
    --index-dirs a,b        索引目录名（默认 00-总览）
    --min-lines N           笔记最少行数（默认 0 即不检查）
    --max-lines N           笔记最多行数（默认 0 即不检查）

退出码：0 = 全部通过；1 = 有检查项未通过。

设计目标：跨平台、无第三方依赖、可直接在批量产出过程中反复运行。
"""
from __future__ import annotations

import argparse
import os
import re
import sys

# 默认排除：隐藏目录、附件、模板、素材类目录
DEFAULT_EXCLUDE = {
    ".obsidian", ".git", ".workbuddy", ".trash", ".archive",
    "99-附件", "附件", "assets", "attachments",
    "99-模板", "模板", "templates",
}

# 跨工具兼容的 callout 类型（GitHub Alert 5 种，大小写不敏感）
PUBLIC_CALLOUTS = {"note", "tip", "important", "warning", "caution"}

WIKILINK_RE = re.compile(r"\[\[([^\]\|#]+)")
CALLOUT_RE = re.compile(r"\[!([A-Za-z]+)\]")
FENCE_RE = re.compile(r"```.*?```", re.S)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


HEADING_RE = re.compile(r"^#{1,6}\s+.*$", re.M)


def headings(text: str) -> list[str]:
    return HEADING_RE.findall(text)


def strip_code(text: str) -> str:
    """去掉围栏代码块与行内代码，避免把"文档里举例说明的语法"误判为实际使用。"""
    text = FENCE_RE.sub("", text)
    text = INLINE_CODE_RE.sub("", text)
    return text


def collect_md(root: str, excludes: set[str]) -> list[str]:
    out: list[str] = []
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in excludes and not d.startswith(".")]
        for fn in fns:
            if fn.endswith(".md"):
                out.append(os.path.join(dp, fn).replace("\\", "/"))
    return sorted(out)


def read(path: str) -> str:
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


def classify(root: str, files: list[str], index_dirs: set[str]) -> tuple[list[str], list[str]]:
    """按路径把文件分成 笔记 / 非笔记（索引、模板、散落在根的文件）。"""
    notes, others = [], []
    root_abs = os.path.abspath(root).replace("\\", "/")
    for f in files:
        rel = os.path.relpath(os.path.abspath(f), root_abs).replace("\\", "/")
        top = rel.split("/")[0] if "/" in rel else ""
        if not top:                       # 直接放在库根的文件
            others.append(f)
        elif top in index_dirs:           # 索引层
            others.append(f)
        elif re.match(r"^\d", top):       # 以数字开头的章节目录 → 视为笔记
            notes.append(f)
        else:                             # 其他目录（试卷/作业等）
            others.append(f)
    return notes, others


def main() -> int:
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("root")
    ap.add_argument("--expect-notes", type=int, default=None)
    ap.add_argument("--exclude", default="")
    ap.add_argument("--sections", default="")
    ap.add_argument("--index-dirs", default="00-总览")
    ap.add_argument("--min-lines", type=int, default=0)
    ap.add_argument("--max-lines", type=int, default=0)
    ap.add_argument("--strict-sections", action="store_true",
                    help="把标题缺段落视为失败（默认仅警告，因导学/附录类笔记结构本就不同）")
    args = ap.parse_args()

    root = args.root
    if not os.path.isdir(root):
        print(f"[FATAL] 不是目录: {root}")
        return 1

    excludes = set(DEFAULT_EXCLUDE)
    excludes |= {s.strip() for s in args.exclude.split(",") if s.strip()}
    index_dirs = {s.strip() for s in args.index_dirs.split(",") if s.strip()}
    want_sections = [s.strip() for s in args.sections.split(",") if s.strip()]

    files = collect_md(root, excludes)
    names = {os.path.basename(f)[:-3] for f in files}
    notes, others = classify(root, files, index_dirs)

    failures: list[str] = []

    print("=" * 68)
    print(f"库根: {os.path.abspath(root)}")
    print(f"md 文件总数: {len(files)}   其中笔记: {len(notes)}   其他(索引/模板/资料): {len(others)}")

    # 1) 分章计数
    print("\n[1] 分章计数")
    buckets: dict[str, int] = {}
    for f in notes:
        rel = os.path.relpath(os.path.abspath(f), os.path.abspath(root)).replace("\\", "/")
        top = rel.split("/")[0]
        buckets[top] = buckets.get(top, 0) + 1
    for k in sorted(buckets):
        print(f"    {k}: {buckets[k]} 篇")
    if args.expect_notes is not None:
        ok = len(notes) == args.expect_notes
        print(f"    合计 {len(notes)} / 期望 {args.expect_notes}  {'✅' if ok else '❌'}")
        if not ok:
            failures.append(f"笔记总数 {len(notes)} ≠ 期望 {args.expect_notes}")

    # 2) 死链
    print("\n[2] 双链死链")
    broken: dict[str, int] = {}
    for f in files:
        for m in WIKILINK_RE.finditer(strip_code(read(f))):
            t = m.group(1).strip()
            if t and t not in names:
                broken[t] = broken.get(t, 0) + 1
    if broken:
        print(f"    ❌ {len(broken)} 条未解析链接:")
        for t in sorted(broken)[:40]:
            print(f"       {t}")
        if len(broken) > 40:
            print(f"       …（另有 {len(broken) - 40} 条）")
        failures.append(f"死链 {len(broken)} 条")
    else:
        print("    ✅ 无死链")

    # 3) 段落完整度（按"标题行"匹配，避免正文里的同名词蒙混过关）
    if want_sections:
        print("\n[3] 模板段落完整度")
        bad = []
        for f in notes:
            hs = headings(read(f))
            miss = [s for s in want_sections if not any(s in h for h in hs)]
            if miss:
                bad.append((f, miss))
        if bad:
            mark = "❌" if args.strict_sections else "⚠️ "
            print(f"    {mark} {len(bad)} 篇的标题中缺段落（导学/附录类常属正常）:")
            for f, miss in bad[:20]:
                print(f"       {os.path.basename(f)}  缺: {'、'.join(miss)}")
            if len(bad) > 20:
                print(f"       …（另有 {len(bad) - 20} 篇）")
            if args.strict_sections:
                failures.append(f"{len(bad)} 篇段落不完整")
        else:
            print(f"    ✅ {len(notes)} 篇段落齐全")
    else:
        print("\n[3] 模板段落完整度  (跳过：未指定 --sections)")

    # 4) 不兼容语法（Obsidian 私有 callout）
    print("\n[4] 不兼容语法残留")
    residue = []
    for f in files:
        for typ in {m.group(1) for m in CALLOUT_RE.finditer(strip_code(read(f)))}:
            if typ.lower() not in PUBLIC_CALLOUTS:
                residue.append((f, typ))
    if residue:
        print(f"    ❌ {len(residue)} 处私有 callout:")
        for f, typ in residue[:20]:
            print(f"       {os.path.basename(f)}  →  [!{typ}]")
        failures.append(f"私有 callout 残留 {len(residue)} 处")
    else:
        print("    ✅ 无私有 callout 残留")

    # 5) 围栏与折叠块配对
    print("\n[5] 代码围栏 / 折叠块配对")
    fence_bad = [f for f in files if read(f).count("```") % 2]
    det_bad = [f for f in files if read(f).count("<details>") != read(f).count("</details>")]
    if fence_bad:
        print(f"    ❌ 围栏不配对 {len(fence_bad)} 篇: " + "、".join(os.path.basename(x) for x in fence_bad[:10]))
        failures.append(f"围栏不配对 {len(fence_bad)} 篇")
    else:
        print("    ✅ 围栏全部成对")
    if det_bad:
        print(f"    ❌ <details> 不配对 {len(det_bad)} 篇: " + "、".join(os.path.basename(x) for x in det_bad[:10]))
        failures.append(f"<details> 不配对 {len(det_bad)} 篇")
    else:
        print("    ✅ <details> 全部配对")

    # 6) frontmatter
    print("\n[6] frontmatter")
    nofm = [f for f in files if not read(f).startswith("---")]
    if nofm:
        print(f"    ⚠️  {len(nofm)} 个文件无 frontmatter: " + "、".join(os.path.basename(x) for x in nofm[:10]))
        failures.append(f"{len(nofm)} 个文件缺 frontmatter")
    else:
        print("    ✅ 全部具备 frontmatter")

    # 7) 篇幅
    if notes:
        Ls = [len(read(f).splitlines()) for f in notes]
        print(f"\n[7] 篇幅: 最短 {min(Ls)} / 最长 {max(Ls)} / 平均 {sum(Ls) // len(Ls)} 行")
        if args.min_lines and min(Ls) < args.min_lines:
            failures.append(f"存在短于 {args.min_lines} 行的笔记（最短 {min(Ls)}）")
            print(f"    ❌ 有笔记短于 {args.min_lines} 行")
        if args.max_lines and max(Ls) > args.max_lines:
            failures.append(f"存在长于 {args.max_lines} 行的笔记（最长 {max(Ls)}）")
            print(f"    ❌ 有笔记长于 {args.max_lines} 行")

    print("\n" + "=" * 68)
    if failures:
        print("结论: ❌ 未通过")
        for x in failures:
            print(f"  - {x}")
        return 1
    print("结论: ✅ 全部通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())
