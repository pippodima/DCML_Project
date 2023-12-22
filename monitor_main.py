import time

from pc_monitor import monitor
from mouse_monitor import MouseMonitor
from keyboard_monitor import KeyboardMonitor
import threading


def start_monitor():
    keyboard_monitor = KeyboardMonitor()
    keyboard_monitor.start()
    mouse_monitor = MouseMonitor()
    mouse_monitor.start()
    time.sleep(10)
    # monitor(duration=15, MEMORY=None)


if __name__ == "__main__":
    start_monitor()

#  TODO: provare a salvare la posizione del mouse una volta ogni t tempo

