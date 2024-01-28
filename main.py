from Monitoring.CompleteMonitor import CompleteMonitor
import time
import pickle
import subprocess
import winsound

monitor_only = False


def beep():
    try:
        subprocess.Popen(["afplay", "/System/Library/Sounds/Ping.aiff"])
    except FileNotFoundError:
        winsound.Beep(frequency=1000, duration=300)


if __name__ == "__main__":
    count = 0
    interval = 0.5
    monitor = CompleteMonitor(interval=interval, verbose=False)
    monitor.start_monitor()
    try:
        if not monitor_only:
            time.sleep(2)
            with open('ML/TrainedModelsNoCPU_RAM/RandomForest.pkl', 'rb') as file:
                classifier = pickle.load(file)
                while True:
                    pred = classifier.predict(monitor.get_realTime_data())
                    print(pred)
                    count = count + 1 if pred == 1 else 0
                    if count >= 5:
                        beep()
                    time.sleep(interval)
        else:
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                monitor.stop()
                print("stopped")

    except KeyboardInterrupt:
        monitor.stop()
        print("Monitoring stopped by user.")

