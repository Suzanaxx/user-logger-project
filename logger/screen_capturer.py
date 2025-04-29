import pyautogui
import time
import os

def start_screen_capture(interval=60):
    os.makedirs("logs", exist_ok=True)
    i = 0
    try:
        while True:
            screenshot = pyautogui.screenshot()
            filename = f"logs/screen_{i}.png"
            screenshot.save(filename)
            print(f"Zajet zaslon: {filename}")
            i += 1
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Zajem prekinjen.")
