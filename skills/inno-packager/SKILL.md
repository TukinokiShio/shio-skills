---
name: inno-packager
description: Build and troubleshoot Windows installers with Inno Setup 6. Use for .iss scripts, ISCC compilation, shortcuts, registry entries, uninstall behavior, and installer diagnostics.
permissions:
  - file_read
  - file_write
  - env
  - shell
  - local_command_after_user_confirmation
---

# Inno Packager

Use this skill when packaging a Windows desktop application as an Inno Setup installer.

## Requirements

- Windows;
- Inno Setup 6 installed;
- `ISCC.exe` available on `PATH`, or an explicit compiler path passed to the helper script;
- the application build and all files referenced by `[Files]` already available.

The skill does not assume a particular installation directory. Common locations include the official Inno Setup directory under `Program Files` or a user-selected installation path.

## Minimal installer

```iss
[Setup]
AppName=MyApp
AppVersion=1.0.0
DefaultDirName={autopf}\MyApp
OutputDir=.

[Files]
Source: "MyApp.exe"; DestDir: "{app}"

[Icons]
Name: "{group}\MyApp"; Filename: "{app}\MyApp.exe"
```

## Compile

Use the bundled helper:

```powershell
python scripts/iscc_compile.py installer.iss
python scripts/iscc_compile.py installer.iss --output .\dist
python scripts/iscc_compile.py installer.iss --iscc "C:\Path\To\ISCC.exe"
```

The helper checks the explicit path first, then `ISCC.exe` on `PATH`, then standard Windows installation locations. It passes preprocessor definitions with `--define NAME=VALUE` and returns the compiler exit code.

## Workflow

1. Identify the executable, runtime files, assets, and required redistributables.
2. Create or update `[Setup]`, `[Files]`, `[Icons]`, `[Run]`, and `[Uninstall*]` sections as needed.
3. Use `{app}`, `{userappdata}`, `{autopf}`, and other Inno constants instead of machine-specific paths.
4. Compile and inspect the compiler output.
5. Test install, upgrade, shortcut launch, uninstall, and rollback behavior on a clean Windows environment.

## Safety and reliability

- Treat `.iss` files and Pascal Script as executable build input; review `[Run]`, `[UninstallRun]`, `Exec`, `ShellExec`, and registry operations before compiling.
- Do not place secrets, personal paths, or machine-specific credentials in installer scripts.
- Prefer relative `Source:` paths rooted at the script directory.
- Keep signing and release credentials outside the installer project.
- Do not claim an installer is production-ready without testing installation and uninstallation on a clean machine.

## Common failures

- `ISCC.exe not found`: install Inno Setup or pass `--iscc` explicitly.
- Missing source file: check relative paths and the current script directory.
- Unknown constant: verify the constant is supported by the installed Inno Setup version.
- Upgrade problems: test `AppId`, versioning, overwrite behavior, and uninstall settings.

## Scope

This skill creates and diagnoses Inno Setup scripts. It does not build the application, sign binaries, distribute installers, or publish releases.
