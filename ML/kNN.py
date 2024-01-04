import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split

filepath = "copy_FirstGame.csv"
filepath_anomaly = "ezbot.csv"
df = pd.read_csv(filepath)
df['anomaly'] = 0
df_anomaly = pd.read_csv(filepath_anomaly)
df_anomaly['anomaly'] = 1

df[['MOUSE_X', 'MOUSE_Y']] = df['MOUSE_POSITION'].str.strip('()').str.split(', ', expand=True).astype(int)
df.drop('MOUSE_POSITION', axis=1, inplace=True)

df_anomaly[['MOUSE_X', 'MOUSE_Y']] = df_anomaly['MOUSE_POSITION'].str.strip('()').str.split(', ', expand=True).astype(int)
df_anomaly.drop('MOUSE_POSITION', axis=1, inplace=True)

combined_df = pd.concat([df, df_anomaly], ignore_index=True)

X = combined_df[['CPU', 'MEMORY', 'MOUSE_X', 'MOUSE_Y', 'LEFT_CLICKS', 'RIGHT_CLICKS', 'q', 'w', 'e', 'r', 't', 'd', 'f', 'tab', 'space', 'ctrl']]
Y = combined_df[['anomaly']]
x_Train, x_Test, y_Train, y_Test = train_test_split(X, Y, test_size=0.2, shuffle=False)


classifier = KNeighborsClassifier()
classifier.fit(x_Train, y_Train)

preditions = classifier.predict(x_Test)

print(accuracy_score(y_Test, preditions))
