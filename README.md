# AutoGUI Exercise

A tiny script that periodically presses the Shift key to keep a Windows session active.

Files
- `autoguiexercise.py`: main script. It sends a Shift key press every set interval and logs start/end times and total presses.
- `requirements.txt`: Python dependencies for the project.

Installation (terminal)
1. Open terminal.
2. (Optional but recommended) Create and activate a virtual environment:

```terminal
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:
```terminal
py -m pip install -r requirements.txt
```

```terminal
py -m pip install -r requirements.txt
```

Usage

Run the script from the project folder:

```terminal
py .\autoguiexercise.py
```

The script prints a start timestamp, presses Shift periodically, and logs the end timestamp and duration when you stop it with Ctrl+C.

Configuration
- By default the script waits 200 seconds between presses. Change the `time.sleep(200)` value in `autoguiexercise.py` to adjust frequency.

Safety and permissions
```terminal
py .\autoguiexercise.py
```

The script prints a start timestamp, presses Shift periodically, and logs the end timestamp and duration when you stop it with Ctrl+C.

Configuration
- By default the script waits 200 seconds between presses. Change the `time.sleep(200)` value in `autoguiexercise.py` to adjust frequency.

Safety and permissions
- The script controls keyboard input using `pyautogui`. Keep focus on a safe window when running.
- On some systems additional permissions or UAC prompts may be needed to allow synthetic input. If you run into permission errors, run terminal as Administrator.

Packaging to a Windows executable
--------------------------------

This repository includes two helpers to build a standalone Windows executable (EXE): a PowerShell script `build_exe.ps1` and a cross-platform Python helper `build.py`.

PowerShell (recommended on Windows)

1. Open PowerShell in this project folder.
2. (Optional) Run as Administrator if you need to install system packages.
3. Run:

```powershell
.\build_exe.ps1 -Clean
```

This will create a `.venv` virtual environment, install dependencies from `requirements.txt`, install `pyinstaller`, and run PyInstaller to produce a single-file `autoguiexercise.exe` in the `dist\` folder.

Python helper (cross-platform)

You can also run the Python helper which performs the same steps programmatically:

```powershell
# create venv and build (from project root)
py -3 build.py --clean --onefile
```

Notes
- The produced executable is a single-file binary when `--onefile` is used. The first launch may take a few seconds while the bundled app unpacks.
- Antivirus or Windows SmartScreen may warn about unsigned binaries. If you distribute the exe publicly, consider code signing.
- Building produces folders `build/`, `dist/` and a spec file `autoguiexercise.spec` in the project root. Use the `-Clean` flag to remove previous builds before packaging.
