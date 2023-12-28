from pynput import mouse
import time
from threading import Timer

class MouseMonitor:
    def __init__(self, interval):
        self.listener = mouse.Listener(on_click=self.on_click)
        self.interval = interval
        self.left_clicks = 0
        self.right_clicks = 0

    def start(self):
        self.listener.start()
        self.schedule_print_counts_and_position()

    def stop(self):
        self.listener.stop()

    def on_click(self, x, y, button, pressed):
        if button == mouse.Button.left:
            if pressed:
                self.left_clicks += 1
        elif button == mouse.Button.right:
            if pressed:
                self.right_clicks += 1


    def print_counts_and_position(self):
        print(f"Mouse Position: {mouse.Controller().position}")
        print(f"Left Clicks: {self.left_clicks}")
        print(f"Right Clicks: {self.right_clicks}")
        print("------")

        # Reset counts for the next second
        self.left_clicks = 0
        self.right_clicks = 0

        # Schedule the function to run again after 1 second
        self.schedule_print_counts_and_position()

    def schedule_print_counts_and_position(self):
        # Schedule the print function to run periodically
        Timer(self.interval, self.print_counts_and_position).start()


