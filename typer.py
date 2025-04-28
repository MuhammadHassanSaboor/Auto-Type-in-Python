# pip install pyautogui
import pyautogui
import time

print("You have 3 seconds to open Vs Code where you want to type")

time.sleep(3)

code = [

    "a = 10",
    "if a == 10:",
    "print(\"Yes\")",
]

for line in code:
    pyautogui.write(line , interval = 0.1)
    pyautogui.press('enter')
    time.sleep(0.1)

