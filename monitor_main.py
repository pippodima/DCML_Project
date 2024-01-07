import warnings

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


if __name__ == "__main__":
    interval = 0.5
    monitor = CompleteMonitor(interval=interval, verbose=False)
    monitor.start_monitor()
    time.sleep(2)
    print(monitor.get_realTime_data())
    try:
        with open('ML/TrainedModels/RandomForest.pkl', 'rb') as file:
            classifier = pickle.load(file)
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                while True:
                    pred = classifier.predict(monitor.get_realTime_data())
                    print(pred)
                    if pred == 1:
                        count += 1
                    else:
                        count = 0
                    if count >= 30:
                        beep()
                    time.sleep(interval)
    except KeyboardInterrupt:
        monitor.stop()
        print("Monitoring stopped by user.")



