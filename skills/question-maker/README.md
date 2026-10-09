# question-maker

Create evidence-grounded questions, practice sets, and exam papers from textbooks, course notes, syllabi, and other learning materials.

## When to use it

Use this skill when an agent needs to write or assemble questions, answer keys, worked explanations, or scoring rubrics from supplied learning materials.

## Delivery format

- For questions embedded in a study note, keep the questions and their answers/explanations in the same Markdown document.
- For a quiz, test, or exam paper, produce separate Markdown files for the candidate paper and the answer key with explanations. Keep question IDs stable across both files.

## Required visuals

The skill treats visual completeness as a required quality gate. First inspect the in-scope source material and identify which visuals are part of the learning objectives. When a question requires reading or interpreting a chart, diagram, or other visual, create and embed the actual visual, include its asset with the deliverable, verify its link, and preview it. Text that merely describes a missing graph does not satisfy a visual question. Statistical plots must be reproducible and must not be fabricated with generative image tools. If a required visual cannot be created or checked, report the result as partial.

## Tool and renderer requirements

The agent needs tools to read the supplied files and, where applicable, create charts or diagrams and preview the result. The skill does not install tools or plugins automatically. LaTeX formulas may require MathJax/KaTeX, and Mermaid diagrams may require a compatible renderer or plugin; document these dependencies and provide a plain-text fallback when the target reader may not support them.

## Review and model routing

The skill defines role contracts for question writing, independent review, adversarial critique, and integration. If independent subagents are unavailable, report `SINGLE_AGENT_REVIEW` as the review mode and do not claim a full independent adversarial review. Its default model route is GPT-6 Luna at very high reasoning; GPT-6.1 Sol is considered only for irreducibly complex, long-horizon reasoning and requires explicit user authorization.

See [SKILL.md](SKILL.md) for the complete workflow and quality gates.
