## Description
A Basic keylogger program that records and logs keystrokes. Focus on logging the keys pressed and saving them to a file.

**Requirements:**
Install the pynput library if not already installed:

     pip Install pynput

### How It Works:

1. **Execution**:
    - Run the script (`python keylogger_tool.py`).
    - The program starts listening for keyboard input.
    - The log file `key_log.txt` is created in the same directory as the script.
2. **Keystroke Logging**:
    - Any keystroke made while the script runs is added to the `key_log` variable.
    - Every 10 seconds, the logged keystrokes are written to `key_log.txt`.
3. **Stopping the Keylogger**:
    - Press `Ctrl+C` in the terminal to stop the program manually.

---

###
     
