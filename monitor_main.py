from CompleteMonitor import CompleteMonitor

if __name__ == "__main__":
    interval = 1
    monitor = CompleteMonitor(interval=interval, verbose=True)
    monitor.start_monitor()
