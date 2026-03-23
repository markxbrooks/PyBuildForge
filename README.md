# PyBuildForge

**PyBuildForge** is a cross-platform build system designed to transform Python projects into standalone, distributable executables with minimal configuration.

---

## Overview

PyBuildForge provides a unified interface for building Python applications across multiple operating systems. It abstracts away platform-specific build steps and integrates with packaging tools such as PyInstaller to produce portable binaries.

Key goals:

* Cross-platform consistency (Linux, macOS, Windows)
* Minimal configuration for rapid onboarding
* Structured build pipeline with clear logging
* Extensibility for custom build steps

---

## Features

* Cross-platform build orchestration
* Integrated logging and diagnostics
* Automated cleanup of previous builds
* PyInstaller-based packaging
* Modular architecture for extensibility

---

## Installation

Clone the repository:

```bash
git clone https://github.com/markxbrooks/PyBuildForge.git
cd PyBuildForge
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the build system:

```bash
python -m building.buildsys 2>&1 | head -50
```

### Example Output

```text
Building on: linux
Project root: /home/brooks/PycharmProjects/JDXI-Editor
╭─────────── linux builder ────────────╮
│  linux builder Application Starting  │
╰──────────────────────────────────────╯
[02/10/26 23:12:10] INFO  linux builder starting up with log file /home/brooks/.linux builder/logs/linux builder-10Feb2026-23-12-10.log...
INFO  🎹 JD-Xi Editor v0.9.6 - Linux Build System
INFO  ==================================================
INFO
🧹 Cleaning previous builds...
INFO
📦 Building with PyInstaller...
INFO  This may take a few minutes...
```

---

## Build Pipeline

The build process typically consists of:

1. Environment detection (OS, paths, configuration)
2. Cleanup of previous build artifacts
3. Packaging via PyInstaller
4. Output validation and logging

---

## Logging

PyBuildForge generates detailed logs for each build session. Logs are stored in a user-specific directory:

```
~/.<platform> builder/logs/
```

These logs include timestamps, build steps, and diagnostic information to assist with debugging and reproducibility.

---

## Configuration

Configuration is designed to be minimal but extensible. Future enhancements may include:

* Custom build hooks
* Plugin-based architecture
* CI/CD pipeline integration

---

## Roadmap

* [ ] Windows and macOS builder parity
* [ ] Plugin system for custom bui
