# question-maker

**Version:** 2.0.0

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

## Orchestration and review

For exams, tests, larger question sets, or work with strict coverage and scoring requirements, the default is two independent writers producing competing candidates followed by one independent verifier. The verifier first solves without seeing the answer key, then checks for evidence-based defects. A small, low-stakes set of examples embedded in study notes can use one writer and one necessary verification; note format alone does not imply the lighter workflow.

Correctness, substantive ambiguity, scope, answerability, scoring, source support, and required visuals are hard quality gates. Creativity and other quality traits help select among candidates that pass those gates. A defect may trigger at most one targeted correction and a recheck of affected parts. An uncertain claim gets one targeted source or tool check; unresolved candidates are set aside. Do not run open-ended debate. The two writers may run in parallel or in sequence, but their contexts must remain isolated. If a second independent writer is unavailable, do not call the run B; use A only for low-stakes note examples, otherwise report a partial result. If an independent verifier is unavailable, mark `SINGLE_AGENT_REVIEW` and do not claim independent verification; if it is explicitly required, report a partial result.

See [SKILL.md](SKILL.md) for the complete workflow and quality gates.
