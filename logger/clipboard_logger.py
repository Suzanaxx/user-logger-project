import pyperclip
import logging
import time
import os
from datetime import datetime

# Ustvari mapo za loge
os.makedirs("logs", exist_ok=True)

# Nastavi logging
log_filename = f"logs/clipboard_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='%(asctime)s: %(message)s')

clipboard_history = set()
stop_flag = False  # globalni signal za ustavitev

def start_clipboard_logging(interval=5):
    global stop_flag
    stop_flag = False
    try:
        while not stop_flag:
            content = pyperclip.paste()
            if content and content not in clipboard_history:
                clipboard_history.add(content)
                logging.info(f"Clipboard content: {content}")
            time.sleep(interval)
    except Exception as e:
        logging.error(f"Napaka pri beleženju odložišča: {e}")

def stop_clipboard_logging():
    global stop_flag
    stop_flag = True
