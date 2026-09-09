# Reference-First Dev

An agent skill for finding proven implementations before designing a new project, feature, or module. It ranks candidates using technical fit, maintenance evidence, community evidence, implementation quality, and license constraints.

## Use it when

- starting a non-trivial project or module;
- asking whether an existing implementation or package already exists;
- comparing libraries or reference repositories;
- deciding whether to reuse, adapt, or independently reimplement a solution.

## Output

The skill produces a ranked candidate table, explicit assumptions, license and safety notes, and a least-risk integration recommendation. Deep inspection happens only after the user selects a candidate.

## Dependencies

No fixed CLI, MCP server, or model is required. The host agent needs a way to perform read-only web or repository research. Repository code and scripts are never executed as part of inspection.

## Limitations

Search results can be incomplete or stale. Stars do not prove quality. License status, maintenance, security, and suitability still require human verification before adoption.

## Example

> Find a maintained reference implementation for resumable uploads in a TypeScript service. Compare official packages and GitHub projects, then recommend whether to depend on one or implement the protocol ourselves.
