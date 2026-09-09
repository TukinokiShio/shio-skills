# Inno Packager

An agent skill for creating and troubleshooting Windows installers with Inno Setup 6.

## What it covers

- `.iss` script structure;
- application files and shortcuts;
- registry and uninstall behavior;
- Pascal Script and preprocessor definitions;
- compiler diagnostics and upgrade testing.

## Requirements

Windows and Inno Setup 6. The included Python helper locates `ISCC.exe` through an explicit `--iscc` path, `PATH`, or common Windows installation directories.

```powershell
python scripts/iscc_compile.py installer.iss --output .\dist
```

## Limits

The skill does not build the application, sign binaries, manage release credentials, or publish installers. Review installer scripts before compiling because Inno Setup supports commands and registry changes.

## Example

> Package `dist/MyApp.exe` as a per-machine installer, create a Start Menu shortcut, preserve user data on upgrade, and verify clean install and uninstall behavior.
