from pynput import mouse

class MouseMonitor:
    def __init__(self):
        self.listener = mouse.Listener(on_move=self.on_move)
    def on_move(self, x, y):
        print(f'Mouse moved to ({x}, {y})')


    def on_click(self, x, y, button, pressed):
        if pressed:
            print(f'Mouse clicked at ({x}, {y}) with {button} button pressed')
        else:
            print(f'Mouse released at ({x}, {y}) with {button} button released')


    def on_scroll(self, x, y, dx, dy):
        print(f'Scrolling at ({x}, {y}) with delta ({dx}, {dy})')

    def start(self):
        self.listener.start()

    def stop(self):
        self.listener.stop()
