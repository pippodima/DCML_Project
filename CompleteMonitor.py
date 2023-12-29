from pc_monitor import StatsMonitor
from mouse_monitor import MouseMonitor
from keyboard_monitor import KeyboardMonitor
from threading import Timer
import time
import csv


class CompleteMonitor:
    def __init__(self, interval, verbose=False):
        self.interval = interval
        self.stats_monitor = StatsMonitor(interval=self.interval)
        self.mouse_monitor = MouseMonitor(interval=self.interval)

        keys_to_monitor = ['q', 'w', 'e', 'r', 't', 'd', 'f', 'tab', 'space', 'ctrl']
        self.keyboard_monitor = KeyboardMonitor(keys_to_monitor, interval=self.interval)

        self.shared_queue = []
        self.fieldnames = ['TIMESTAMP', 'CPU', 'MEMORY', 'MOUSE_POSITION', 'LEFT_CLICKS', 'RIGHT_CLICKS', 'q', 'w', 'e', 'r', 't', 'd', 'f', 'tab', 'space', 'ctrl']
        self.csvFile = open('new_monitored_values.csv', 'w+')
        self.writer = csv.DictWriter(self.csvFile, fieldnames=self.fieldnames)

        self.log = {}
        self.verbose = verbose


    def start_monitor(self):
        self.writer.writeheader()
        self.keyboard_monitor.start()
        self.mouse_monitor.start()
        self.stats_monitor.start()
        self.schedule_write_row()


    def write_row(self):
        if self.stats_monitor.queue and self.keyboard_monitor.queue and self.mouse_monitor.queue:
            self.log['TIMESTAMP'] = time.time_ns()

            keyboard_data = self.keyboard_monitor.queue.pop()
            mouse_data = self.mouse_monitor.queue.pop()
            stats_data = self.stats_monitor.queue.pop()

            self.log = {**self.log, **stats_data, **mouse_data, **keyboard_data}
            if self.verbose: print(self.log)
            self.writer.writerow(self.log)
        self.schedule_write_row()


    def schedule_write_row(self):
        Timer(self.interval, self.write_row).start()


# TODO: scrivere su file csv self.log