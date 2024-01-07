import pickle
import time
import pandas as pd
from sklearn.model_selection import train_test_split
import subprocess
import winsound

df = pd.read_csv('Data/dataset.csv')
X = df[['CPU', 'MEMORY', 'MOUSE_X', 'MOUSE_Y', 'LEFT_CLICKS', 'RIGHT_CLICKS', 'q', 'w', 'e', 'r', 't', 'd', 'f', 'tab', 'space', 'ctrl']]
Y = df[['anomaly']]
x_Train, x_Test, y_Train, y_Test = train_test_split(X, Y, test_size=0.2, shuffle=True)


with open('TrainedModels/RandomForest.pkl', 'rb') as file:
    classifier = pickle.load(file)

frequency = 1000  # in Hertz
duration = 1000


def beep():
    try:
        subprocess.Popen(["afplay", "/System/Library/Sounds/Ping.aiff"])
    except FileNotFoundError:
        winsound.Beep(frequency, duration)


count = 0
beep()

for i in range(1, x_Test.shape[0]):
    print(classifier.predict([x_Test.values[i]]))
    print(y_Test.values[i])
    if classifier.predict([x_Test.values[i]]) == 1:
        count += 1
    else:
        count = 0
    print('count: ', count)
    if count >= 30:
        beep()
    time.sleep(0.5)
