from CompleteMonitor import CompleteMonitor
import time
import pickle
import subprocess
import winsound


def beep():
    try:
        subprocess.Popen(["afplay", "/System/Library/Sounds/Ping.aiff"])
    except FileNotFoundError:
        winsound.Beep(frequency=1000, duration=300)


monitor_only = False
if __name__ == "__main__":
    count = 0
    interval = 0.1
    monitor = CompleteMonitor(interval=interval, verbose=True)
    monitor.start_monitor()
    try:
        if not monitor_only:
            time.sleep(2)
            with open('ML/TrainedModels/RandomForest.pkl', 'rb') as file:
                classifier = pickle.load(file)
                while True:
                    time.sleep(interval*10)
                    pred = classifier.predict(monitor.get_realTime_data())
                    print(pred)
                    count = count + 1 if sum(pred) >= 5 else 0
                    if count >= 2:
                        beep()
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

