from pynput import mouse
from threading import Timer


class MouseMonitor:
    def __init__(self, interval, verbose=False):
        self.listener = mouse.Listener(on_click=self.on_click)
        self.interval = interval
        self.left_clicks = 0
        self.right_clicks = 0
        self.log = {'MOUSE_X': 0, 'MOUSE_Y': 0, 'LEFT_CLICKS': 0, 'RIGHT_CLICKS': 0}
        self.queue = []
        self.verbose = verbose
        self.arrest = False

    def start(self):
        self.listener.start()
        self.schedule_print_counts_and_position()

    def stop(self):
        self.listener.stop()
        self.arrest = True

    def on_click(self, x, y, button, pressed):
        if button == mouse.Button.left:
            if pressed:
                self.log['LEFT_CLICKS'] += 1
                self.left_clicks += 1
        elif button == mouse.Button.right:
            if pressed:
                self.right_clicks += 1
                self.log['RIGHT_CLICKS'] += 1


    def print_counts_and_position(self):
        if self.verbose:
            print(f"Mouse X: {self.log['MOUSE_X']}")
            print(f"Mouse Y: {self.log['MOUSE_Y']}")
            print(f"Left Clicks: {self.log['LEFT_CLICKS']}")
            print(f"Right Clicks: {self.log['RIGHT_CLICKS']}")
            print("------")

        self.log['MOUSE_X'] = mouse.Controller().position[0]
        self.log['MOUSE_Y'] = mouse.Controller().position[1]
        self.queue.append(self.log.copy())

        self.log['LEFT_CLICKS'] = 0
        self.log['RIGHT_CLICKS'] = 0

        if not self.arrest: self.schedule_print_counts_and_position()

    def schedule_print_counts_and_position(self):
        Timer(self.interval, self.print_counts_and_position).start()


