import threading
import tkinter as tk
from tkinter import messagebox
from logger import screen_capturer, keyboard_logger, clipboard_logger

screen_thread = None
clipboard_thread = None

def start_screen():
    global screen_thread
    if not screen_thread or not screen_thread.is_alive():
        screen_thread = threading.Thread(target=screen_capturer.start_screen_capture, args=(30,), daemon=True)
        screen_thread.start()
        messagebox.showinfo("Zagon", "Zajem zaslona se je začel.")

def stop_screen():
    screen_capturer.stop_screen_capture()
    messagebox.showinfo("Ustavljen", "Zajem zaslona ustavljen.")

def start_keyboard():
    threading.Thread(target=keyboard_logger.start_logging, daemon=True).start()
    messagebox.showinfo("Zagon", "Beleženje tipk se je začelo.")

def stop_keyboard():
    keyboard_logger.stop_logging()
    messagebox.showinfo("Ustavljen", "Beleženje tipk ustavljeno.")

def start_clipboard():
    global clipboard_thread
    if not clipboard_thread or not clipboard_thread.is_alive():
        clipboard_thread = threading.Thread(target=clipboard_logger.start_clipboard_logging, args=(5,), daemon=True)
        clipboard_thread.start()
        messagebox.showinfo("Zagon", "Beleženje odložišča se je začelo.")

def stop_clipboard():
    clipboard_logger.stop_clipboard_logging()
    messagebox.showinfo("Ustavljen", "Beleženje odložišča ustavljeno.")


root = tk.Tk()
root.title("User Logger GUI")

frame = tk.Frame(root, padx=50, pady=50)
frame.pack()

tk.Label(frame, text="Zajem zaslona:", font="Bold").pack()
tk.Button(frame, text="Začni zajem zaslona", command=start_screen).pack(pady=2)
tk.Button(frame, text="Ustavi zajem zaslona", command=stop_screen).pack(pady=2)

tk.Label(frame, text="Zajem tipk:", font="Bold").pack(pady=(10, 0))
tk.Button(frame, text="Začni beleženje tipk", command=start_keyboard).pack(pady=2)
tk.Button(frame, text="Ustavi beleženje tipk", command=stop_keyboard).pack(pady=2)

tk.Label(frame, text="Zajem odložišča:", font="Bold").pack(pady=(10, 0))
tk.Button(frame, text="Začni beleženje odložišča", command=start_clipboard).pack(pady=2)
tk.Button(frame, text="Ustavi beleženje odložišča", command=stop_clipboard).pack(pady=2)

tk.Button(frame, text="Izhod", command=root.destroy, fg="red").pack(pady=10)

root.mainloop()
