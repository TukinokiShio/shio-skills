---
name: dependency-setup
description: >
  Prepare missing project tools and dependencies safely. Use this skill whenever a
  task needs pytest, PyYAML, test/build tools, package-manager dependencies, a
  virtual environment, or any other missing development dependency. First inspect
  the project and produce an installation assessment; never execute a real install,
  create an environment, or change package files until the user gives explicit,
  current-turn authorization naming the intended scope. After authorization, use
  the project's declared dependency manager, verify the result, and report failures
  instead of silently skipping the task.
compatibility: Windows PowerShell; project-specific package managers and runtimes when present.
---

# Dependency setup with an approval gate

Use this skill to close the loop when a required tool or library is missing. The
skill has two deliberately separate phases:

1. **Assessment**: read-only discovery and an installation proposal.
2. **Installation and verification**: only after explicit user authorization.

The user's request to “run the tests”, “fix the environment”, or “make it work”
does not by itself authorize installing packages. A package install, virtual
environment creation, lockfile change, global tool install, or system change is a
state-changing operation and must wait at the approval gate.

## Non-negotiable safety boundary

- Do not run `pip install`, `uv sync`, `poetry install`, `npm install`, `npm ci`,
  `pnpm install`, `yarn install`, package-manager bootstrap commands, or equivalent
  mutating commands during assessment.
- Do not create `.venv`, `venv`, `node_modules`, package caches, lockfiles, or other
  installation artifacts before authorization. Read-only checks and directory
  inspection are allowed.
- Do not install globally, use administrator privileges, alter PATH, configure a
  new package source, or download an unpinned tool without separate, explicit
  authorization for that scope.
- Do not guess a distribution name from an import name when the project does not
  declare the mapping. For example, `yaml` is an import name; the distribution
  must be confirmed from project metadata or an authoritative project source.
- Never treat a failed installation or unavailable network as permission to skip a
  required test silently. Report the blocked state and the exact unverified checks.
- Authorization remains subject to host, sandbox, security, project, and
  administrator constraints.

## Phase A — read-only assessment

Run only commands that inspect state. Keep the assessment short and reproducible.

### 1. Establish whether installation is actually needed

- Identify the requested outcome: test, lint, build, type check, packaging, or
  another operation.
- Check whether the command already exists and which interpreter it belongs to.
  On Windows, prefer `Get-Command`, `where.exe`, and interpreter-qualified checks
  such as `python -m pytest --version` over assuming PATH is correct.
- If the tool is present and usable, continue with the task; do not install a
  duplicate copy.
- If the tool is missing, determine whether it is a hard prerequisite or whether a
  valid existing project command provides the same check.

### 2. Read project declarations before proposing packages

Inspect only files relevant to dependency ownership, such as:

- Python: `pyproject.toml`, `requirements*.txt`, `setup.cfg`, `Pipfile*`,
  `poetry.lock`, `uv.lock`, `environment.yml`, and project instructions.
- Node: `package.json`, `package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`,
  `bun.lock*`, and project instructions.
- Other ecosystems: use the ecosystem's manifest and lockfile only when present;
  otherwise stop at assessment and state that the installation route is unknown.

Record the exact declaration, group/extra, version constraint, and lockfile that
would own the dependency. Prefer the project's existing manager and constraints.
Do not silently add a new dependency declaration merely to make a command run.

### 3. Determine the target environment

Report:

- active runtime and version;
- project-local environment already present, if any;
- package manager and version, if any;
- intended installation location;
- whether the operation would modify source-controlled files, lockfiles, caches,
  global state, or system state;
- prerequisites that are themselves missing.

If the project has an existing environment, prefer using it. If no environment
exists, propose an isolated environment rather than a global install, but treat
creating it as part of the authorization request.

### 4. Produce an authorization request

Before any mutating command, show a concise assessment with this structure:

```text
依赖评估
- 目标：<what the task needs>
- 缺失项：<tool/distribution and evidence>
- 来源：<manifest, lockfile, or explicitly unknown>
- 目标环境：<existing environment or proposed isolated environment>
- 计划命令：<exact commands, including working directory>
- 预计变更：<files, environment, lockfile, global/system impact>
- 风险与回滚：<network/source, version, permissions, removal or restore plan>
- 安装后验证：<exact probe and test command>

是否授权按上述范围执行安装/环境创建？请明确说明目标范围，例如：
“授权将项目声明的 Python 开发依赖安装到该项目的 .venv，不修改全局环境。”
```

Do not continue into installation in the same turn as this request. If the user
authorizes only part of the proposal, narrow the plan and restate the remaining
scope before executing.

## Phase B — authorized installation

Proceed only when the user has given an unambiguous authorization in the current
task. The authorization must cover the target environment and operation; a vague
“继续” is insufficient if multiple scopes were proposed.

### Python routing

Use the project's declared route, in this order of preference:

1. `uv.lock` / documented uv workflow → use the project's documented `uv` command.
2. Poetry metadata and lockfile → use the documented Poetry workflow.
3. Pipenv metadata and lockfile → use the documented Pipenv workflow.
4. A declared `requirements*.txt` → use the selected interpreter's
   `python -m pip install -r <declared-file>`.
5. A declared `pyproject.toml` extra or editable project install → use the exact
   declared extra, such as `python -m pip install -e ".[dev]"`, only when the
   project metadata or documentation supports it.

Rules for Python:

- Bind pip to the chosen interpreter with `python -m pip`; do not use an unrelated
  bare `pip`.
- Prefer an existing project-local `.venv`/`venv`; create one only if authorized.
- Install declared versions and extras. Do not upgrade unrelated packages.
- Do not replace an existing lockfile or regenerate it unless that was explicitly
  authorized.
- If no declaration exists, stop and ask for authorization to install the exact
  proposed distribution(s) and version policy; never infer a package from a bare
  import without evidence.
- For `pytest`/`PyYAML`-type cases, distinguish the executable/import check from
  the distribution name and verify both after installation.

### Node routing

Select the manager from the repository's `packageManager` field, lockfile, or
project instructions. Prefer frozen/locked installation when supported:

- `package-lock.json` → the documented npm locked workflow, normally `npm ci`;
- `pnpm-lock.yaml` → the documented pnpm frozen-lockfile workflow;
- `yarn.lock` → the documented Yarn immutable/locked workflow.

Do not delete or regenerate lockfiles, switch package managers, or install global
CLIs unless the authorization explicitly includes that change.

### Other tools and system prerequisites

For compilers, SDKs, OS packages, global CLIs, administrator-required installers,
or package-manager bootstrapping, provide a separate assessment. State that this
is broader than a project-local dependency install and request separate explicit
authorization. If no documented route exists, stop rather than inventing one.

## Verification and reporting

After an authorized installation:

1. Re-check the executable and import/module from the same environment that will
   run the task.
2. Run the originally requested test, build, lint, or check.
3. Inspect the diff and status for unexpected dependency or lockfile changes.
4. Report installed items, exact environment, commands run, verification output,
   failed checks, and anything still unverified.

If installation partially succeeds, do not claim completion. Mark the state as
`PARTIAL` or `BLOCKED`, identify the first failed transition, and give a recovery
or rollback action within the authorized scope.

## State model

Use these states in reasoning and reporting:

```text
ASSESSING
  -> READY_FOR_AUTHORIZATION
  -> NO_INSTALL_NEEDED
  -> BLOCKED (unknown route, missing declaration, or unsupported prerequisite)

READY_FOR_AUTHORIZATION
  -> AUTHORIZED_INSTALL (explicit scope received)
  -> BLOCKED (authorization absent or narrowed)

AUTHORIZED_INSTALL
  -> VERIFYING
  -> PARTIAL / BLOCKED

VERIFYING
  -> COMPLETE
  -> PARTIAL / BLOCKED
```

The terminal report must state which state was reached. “Skipped because the
tool was missing” is not a terminal success state.
