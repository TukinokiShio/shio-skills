# Course Outline → Obsidian Notes

Turn a course syllabus, textbook table of contents, or exam outline into a structured, reviewable Obsidian notes vault — one note per outline item, wired together with an index layer and wikilinks.

## What it does

Given an outline (a list of screenshots, a pasted table of contents, a section list), the skill:

1. reads what it can from local files before asking anything;
2. asks only the 2–3 questions that cannot be answered from evidence (where to put the vault, what the notes are for, how long each note should be);
3. transcribes the outline, counts items per chapter, and checks that multi-image inputs are contiguous (so a numbering gap is attributed to the outline rather than blamed on a missing screenshot);
4. builds the vault skeleton, an index layer, a template, and a sample chapter for review;
5. produces the rest chapter by chapter, running a validator after each chapter.

Every note uses the same seven sections. Two of them are **not optional**, regardless of discipline:

```text
① One-line takeaway
② Derive it from constraints      ← first principles: hard constraint → counterfactual
                                     → rejected alternatives → conclusion
③ Core mechanism
④ Misconceptions and boundaries   ← uncertainty audit: what people get wrong, what
                                     premises the conclusion depends on, edge cases,
                                     confusable neighbours, and explicit fact/inference/unknown labels
⑤ Real-world relevance            ← renamed per discipline (engineering reality, clinical
                                     relevance, practical application, business meaning, ...)
⑥ How it is examined / applied
⑦ Self-test + related notes
```

Section ② stops notes from becoming memorisation; section ④ stops them from silently carrying wrong beliefs. Both work in humanities, medicine, and law — only the source of constraints changes (era conditions, physiological mechanisms, legislative purpose, communicative needs).

## Use it when

- you have an outline — course, textbook, certification syllabus, reading list — and want a complete note set rather than notes written by hand;
- you want notes that survive switching tools: Obsidian, Typora, VS Code, GitHub;
- you are building study material for exams, coursework, or professional certification;
- you want the same workflow applied across subjects, not a one-off structure for a single course.

It stays out of the way for a single short note or a quick lookup.

## What it produces

```text
<vault>/
├── 00-总览/                 index layer: one overview page + one index per chapter
├── 01-<chapter>/            notes, named exactly as in the outline
├── 02-<chapter>/
├── 99-模板/                 the reusable note template
├── 99-附件/
└── <extra dirs>/            e.g. past exam papers, homework, course projects
```

## What it needs

- No third-party Python packages. The validator `scripts/verify_notes.py` uses the standard library only.
- Obsidian is optional. Notes rely on plain Markdown (YAML frontmatter, tables, Mermaid, `<details>`) and never on a plugin to be readable.
- The only cross-tool syntax rules enforced are: GitHub Alert callout types only, `<details>` for collapsible answers, and no vendor-specific folding syntax.

## Limits and failure cases

- **It does not verify facts against the textbook.** It keeps each note self-consistent and aligned with mainstream accounts, and it labels anything inferred as inferred. Spot-check the notes yourself.
- **It does not invent missing sections.** Gaps, duplicate numbering, and odd numbering in the outline are preserved as-is and explained on the index page.
- **It does not modify your existing vaults.** Reading another vault to learn style is read-only; plugin copying is read-source-write-new; the source vault is checked afterwards.
- **It will stop and ask** before creating a vault in an ambiguous location, and after the sample chapter it waits for your confirmation before mass-producing.
- **It is offline.** No network access, nothing sent anywhere.

## Quick example

```bash
# validate a completed vault
python scripts/verify_notes.py "<vault>" --expect-notes 86 \
  --sections "第一性原理,核心机制,查漏补缺,工程现实,408 考点,自测,关联" \
  --min-lines 60 --max-lines 220
```

The validator reports per-chapter counts, broken wikilinks, missing template sections, incompatible callout types, unbalanced code fences and `<details>` blocks, missing frontmatter, and note length. Exit code 1 means at least one check failed.

## Compatibility

Works with any agent runtime that can read files, write files, and run a Python script. No MCP server, no network, no credentials.

Read [`SKILL.md`](SKILL.md) for the full five-phase workflow, the six non-negotiable principles, and the per-discipline adaptation tables.

## License

MIT. See [`LICENSE`](LICENSE).
