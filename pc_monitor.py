import psutil
from threading import Timer


class StatsMonitor:
    def __init__(self, interval, verbose=False):
        self.interval = interval
        self.stats = {'CPU': 0.0, 'MEMORY': 0.0}
        self.queue = []
        self.verbose = verbose

    def start(self):
        self.schedule_print_usage()

    def print_usages(self):
        self.stats['CPU'] = psutil.cpu_percent()
        self.stats['MEMORY'] = psutil.virtual_memory().percent
        if self.verbose:
            print('Stats:')
            for key, value in self.stats.items():
                print(f'{key}: {value}')
            print('--------------')

        self.queue.append(self.stats)

        self.schedule_print_usage()

    def schedule_print_usage(self):
        Timer(self.interval, self.print_usages).start()