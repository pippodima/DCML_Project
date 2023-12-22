from pynput import keyboard


class KeyboardMonitor:

    def __init__(self):
        self.listener = keyboard.Listener(on_press=self.on_press)

    def on_press(self, key):
        try:
            print(f'Key {key.char} pressed')
        except AttributeError:
            print(f'Special key {key} pressed')

    def on_release(self, key):
        print(f'Key {key} released')
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    def start(self):
        self.listener.start()

    def stop(self):
        self.listener.stop()
