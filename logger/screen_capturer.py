import pyautogui
import time
import os

running = True

def start_screen_capture(interval=60):
    os.makedirs("logs", exist_ok=True)
    i = 0
    global running
    running = True
    while running:
        screenshot = pyautogui.screenshot()
        filename = f"logs/screen_{i}.png"
        screenshot.save(filename)
        print(f"Zajet zaslon: {filename}")
        i += 1
        time.sleep(interval)
def stop_screen_capture():
    global running
    running = False
