---
name: inno-packager
description: Build and troubleshoot Windows installers with Inno Setup 6. Use for .iss scripts, ISCC compilation, shortcuts, registry entries, uninstall behavior, and installer diagnostics.
license: MIT
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

## Required Windows shell refresh when installing icons

Whenever an installer changes the application icon or creates/replaces shortcuts that use it, refresh the Windows shell as part of installation:

1. Resolve the actual Desktop and Start Menu folders through Shell Known Folders. Inspect each affected `.lnk` and confirm its `TargetPath` and `IconLocation` point to the installed executable or icon file. Do not assume the Desktop is at a fixed path; it can be redirected.
2. Run `ie4uinit.exe -ClearIconCache`, then notify the shell with `SHChangeNotify(SHCNE_ASSOCCHANGED, SHCNF_IDLIST, NULL, NULL)` and `SHChangeNotify(SHCNE_UPDATEITEM, SHCNF_PATHW | SHCNF_FLUSH, shortcutPath, NULL)` for each changed shortcut. Check the cache-clear command's exit code, but do not treat it as proof that the visible icon refreshed.
3. Re-enumerate the desktop window handles on every run. Locate the current `Progman` → `SHELLDLL_DefView` → `SysListView32` (`FolderView`) chain, send `F5` to the desktop list, then call `RedrawWindow` with `RDW_INVALIDATE | RDW_ERASE | RDW_ALLCHILDREN | RDW_UPDATENOW`. Do not reuse stale window handles or terminate all Explorer processes just to refresh icons.
4. Verify the icon visibly changed on the desktop and re-check the shortcut target and icon path. If it remains stale, diagnose the responsible shell view/cache before considering a controlled restart that preserves open File Explorer windows.

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
