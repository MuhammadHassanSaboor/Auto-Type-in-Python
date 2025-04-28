# Auto Typer Using Python 🐍⌨️

Welcome to the **Auto Typer** project!  
This simple Python script automatically types code into your open editor (like VS Code) using the `pyautogui` library.

## 📂 Project Structure

- `typer.py` — Script that auto-types the code line by line into the active window.
- `main.py` — Sample output file where the code is typed.

## 🚀 How It Works

1. The `typer.py` script gives you **3 seconds** to open your code editor (e.g., VS Code).
2. After 3 seconds, it **automatically starts typing** each line of code with slight intervals.
3. It simulates human-like typing and presses "Enter" after each line.

### Code Snippet That Is Auto-Typed:

```python
a = 10
if a == 10:
    print("Yes")
```

# 🛠️ Requirements

- Python 3.x
- pyautogui

Install it using:

```bash
pip install pyautogui
```

# 📋 Usage

Open your terminal and run:

```bash
python typer.py
```

- Quickly switch to your open code editor within 3 seconds.
- Watch the magic happen as Python auto-types the code!

> Note:
> Be careful where you run this script — it will start typing wherever your cursor is active!

