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
