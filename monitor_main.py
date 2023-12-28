import time

from pc_monitor import monitor
from mouse_monitor import MouseMonitor
from keyboard_monitor import KeyboardMonitor
import threading


def start_keyboard_monitor(interval):
    keys_to_monitor = ['q', 'w', 'e', 'r', 't', 'd', 'f', 'tab', 'space', 'ctrl']

    keyboard_monitor = KeyboardMonitor(keys_to_monitor, interval=interval)
    keyboard_monitor.start()


    # keyboard_monitor_thread = Thread(target=keyboard_monitor.start)
    # keyboard_monitor_thread.start()


def start_mouse_monitor(interval):
    mouse_monitor = MouseMonitor(interval=interval)
    mouse_monitor.start()


def start_monitor(interval):
    start_keyboard_monitor(interval=interval)
    start_mouse_monitor(interval=interval)
    # monitor(duration=15, MEMORY=None, CPU=None)


if __name__ == "__main__":
    interval = 1
    start_monitor(interval=interval)
