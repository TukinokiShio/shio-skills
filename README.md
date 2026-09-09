# shio-skills

Practical skills for AI coding agents.

`shio-skills` is a curated collection of reusable agent skills built to help developers move from a blank prompt to a useful result with less repeated setup.

## Browse the collection

Skills will be published as self-contained directories under [`skills/`](skills/). Each skill is designed to be understandable before installation and useful without requiring the rest of this repository.

| Skill | What it helps with | Status |
| --- | --- | --- |
| [first-principle](skills/first-principle/) | Reduce ambiguity and unnecessary complexity with evidence-driven reasoning. | Available |
| [uncertainty-blindspot-audit](skills/uncertainty-blindspot-audit/) | Surface weak assumptions, missing factors, and the smallest useful validation steps. | Available |

## What to expect from a skill

Every published skill should make these questions easy to answer:

- What problem does it solve?
- When should an agent use it?
- What does it produce or change?
- What tools or dependencies does it need?
- What are its limits and failure cases?
- Can I see a small example before I try it?

## Using a skill

When a skill is published, its own directory will contain the installation and usage instructions. The general pattern is:

```text
skills/
└── <skill-name>/
    ├── SKILL.md
    ├── README.md       # optional: user-facing guide
    ├── references/     # optional: detailed material
    ├── scripts/        # optional: deterministic helpers
    └── examples/       # optional: small working examples
```

Clone the repository, open the skill directory you want, and follow that skill's README. Do not assume that every skill supports every agent runtime; compatibility is documented per skill.

## Design goal

The collection favors focused, composable skills over a large framework. A good skill should be easy to inspect, easy to try, and easy to remove when it is no longer useful.

## License

Licensing is declared per skill. Until a skill is published, this repository makes no blanket license grant for future contents.
