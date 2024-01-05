from CompleteMonitor import CompleteMonitor
import time

if __name__ == "__main__":
    interval = 0.5
    monitor = CompleteMonitor(interval=interval, verbose=True)
    monitor.start_monitor()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        monitor.stop()
        print("Monitoring stopped by user.")
