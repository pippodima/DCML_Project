import pandas as pd
from StatsMonitor import StatsMonitor
from MouseMonitor import MouseMonitor
from KeyboardMonitor import KeyboardMonitor
from threading import Timer
import csv


class CompleteMonitor:
    def __init__(self, interval, verbose=False):
        self.interval = interval
        self.stats_monitor = StatsMonitor(interval=self.interval)
        self.mouse_monitor = MouseMonitor(interval=self.interval)

        keys_to_monitor = ['q', 'w', 'e', 'r', 't', 'd', 'f', 'tab', 'space', 'ctrl']
        self.keyboard_monitor = KeyboardMonitor(keys_to_monitor, interval=self.interval)

        self.fieldnames = ['CPU', 'MEMORY', 'MOUSE_X', 'MOUSE_Y', 'LEFT_CLICKS', 'RIGHT_CLICKS', 'q', 'w', 'e',
                           'r', 't', 'd', 'f', 'tab', 'space', 'ctrl']
        self.csvFile = open('monitored_values.csv', 'w+')
        self.writer = csv.DictWriter(self.csvFile, fieldnames=self.fieldnames, lineterminator='\n')

        self.log = {}
        self.verbose = verbose
        self.lastValues = {}

        self.arrest = False

        self.data_history = []

    def start_monitor(self):
        self.writer.writeheader()
        self.keyboard_monitor.start()
        self.mouse_monitor.start()
        self.stats_monitor.start()
        self.schedule_write_row()

    def write_row(self):
        if self.stats_monitor.queue and self.keyboard_monitor.queue and self.mouse_monitor.queue:
            # self.log['TIMESTAMP'] = time.time_ns()

            keyboard_data = self.keyboard_monitor.queue.pop()
            mouse_data = self.mouse_monitor.queue.pop()
            stats_data = self.stats_monitor.queue.pop()

            self.log = {**self.log, **stats_data, **mouse_data, **keyboard_data}
            self.lastValues = self.log

            self.data_history.append(self.lastValues)
            self.data_history = self.data_history[-10:]

            if self.verbose:
                print(self.log)

            if not self.csvFile.closed:
                self.writer.writerow(self.log)

        if not self.arrest:
            self.schedule_write_row()

    def schedule_write_row(self):
        Timer(self.interval, self.write_row).start()

    def get_realTime_data(self):
        return pd.DataFrame(self.data_history)

    def stop(self):
        self.arrest = True
        self.stats_monitor.stop()
        self.mouse_monitor.stop()
        self.keyboard_monitor.stop()
        self.csvFile.close()
