from pynput import keyboard
from threading import Timer


class KeyboardMonitor:
    def __init__(self, keys, interval, verbose=False):
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.keys = keys
        self.interval = interval
        self.key_counts = {key: 0 for key in keys}
        self.queue = []
        self.verbose = verbose

    def start(self):
        self.listener.start()
        self.schedule_print_counts()

    def stop(self):
        self.listener.stop()

    def on_press(self, key):
        try:
            char = key.char
            if char in self.keys:
                self.key_counts[char] += 1
        except AttributeError:
            pass
        if key == keyboard.Key.tab:
            self.key_counts['tab'] += 1
        elif key == keyboard.Key.space:
            self.key_counts['space'] += 1
        elif key == keyboard.Key.ctrl:
            self.key_counts['ctrl'] += 1


    def print_counts(self):
        if self.verbose:
            print("Key Counts:")
            for key, count in self.key_counts.items():
                print(f"{key}: {count}")
            print("------")

        self.queue.append(self.key_counts)

        # Reset counts for the next second
        self.key_counts = {key: 0 for key in self.keys}

        # Schedule the function to run again after interval time
        self.schedule_print_counts()

    def schedule_print_counts(self):
        # Schedule the print function to run periodically
        Timer(self.interval, self.print_counts).start()



