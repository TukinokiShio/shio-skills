# shio-skills

Practical skills for AI agents.

`shio-skills` is a curated collection of reusable skills for reasoning, research, learning, Windows packaging, decision tracking, and project setup.

## Browse the collection

Published skills live in [`skills/`](skills/) as self-contained directories, with any supporting files they need.

| Skill | What it helps with | Status |
| --- | --- | --- |
| [first-principle](skills/first-principle/) | Break down ambiguous problems and find a clear, evidence-based way forward. | Available |
| [uncertainty-blindspot-audit](skills/uncertainty-blindspot-audit/) | Spot weak assumptions, missing risks, and what to verify in an analysis or plan. | Available |
| [reference-first-dev](skills/reference-first-dev/) | Find and compare existing solutions before building a project or feature. | Available |
| [inno-packager](skills/inno-packager/) | Create and troubleshoot Windows installers with Inno Setup 6. | Available |
| [oq-governance](skills/oq-governance/) | Identify decisions that need user input and track their resolution. | Available |
| [course-outline-to-obsidian](skills/course-outline-to-obsidian/) | Turn course, textbook, or exam outlines into structured Obsidian notes. | Available |
| [dependency-setup](skills/dependency-setup/) | Find and safely prepare missing project tools and dependencies. | Available |

## What to expect from a skill

Every published skill should make these questions easy to answer:

- What problem does it solve?
- When should an agent use it?
- What does it produce or change?
- What tools or dependencies does it need?
- What are its limits and failure cases?
- Can I see a small example before I try it?

## Using a skill

Start with the skill's `SKILL.md` for its purpose and instructions. Some skills also include a `README.md` with a shorter overview or example. The general directory pattern is:

```text
skills/
└── <skill-name>/
    ├── SKILL.md
    ├── README.md       # optional: user-facing guide
    ├── references/     # optional: detailed material
    ├── scripts/        # optional: deterministic helpers
    └── examples/       # optional: small working examples
```

Clone the repository and open the skill directory you want. Compatibility and setup requirements vary by agent runtime, so check the skill's documentation before use.

## Design goal

The collection favors focused, composable skills over a large framework. A good skill should be easy to inspect, easy to try, and easy to remove when it is no longer useful.

## License

Licensing is declared per skill. Check the relevant directory's `LICENSE` before reuse; this repository has no blanket license for the collection.
