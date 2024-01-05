import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

import pickle

filepath = "Data/illaoitop.csv"
filepath2 = "Data/rammustop.csv"

filepath_anomaly = "Data/ezbot.csv"

df = pd.read_csv(filepath)
df['anomaly'] = 0
df2 = pd.read_csv(filepath2)
df2['anomaly'] = 0

df_anomaly = pd.read_csv(filepath_anomaly)
df_anomaly['anomaly'] = 1

df[['MOUSE_X', 'MOUSE_Y']] = df['MOUSE_POSITION'].str.strip('()').str.split(', ', expand=True).astype(int)
df.drop('MOUSE_POSITION', axis=1, inplace=True)

df2[['MOUSE_X', 'MOUSE_Y']] = df2['MOUSE_POSITION'].str.strip('()').str.split(', ', expand=True).astype(int)
df2.drop('MOUSE_POSITION', axis=1, inplace=True)

df_anomaly[['MOUSE_X', 'MOUSE_Y']] = df_anomaly['MOUSE_POSITION'].str.strip('()').str.split(', ', expand=True).astype(int)
df_anomaly.drop('MOUSE_POSITION', axis=1, inplace=True)

combined_df = pd.concat([df, df_anomaly, df2], ignore_index=True)

X = combined_df[['CPU', 'MEMORY', 'MOUSE_X', 'MOUSE_Y', 'LEFT_CLICKS', 'RIGHT_CLICKS', 'q', 'w', 'e', 'r', 't', 'd', 'f', 'tab', 'space', 'ctrl']]
Y = combined_df[['anomaly']]
x_Train, x_Test, y_Train, y_Test = train_test_split(X, Y, test_size=0.2, shuffle=True)

print(x_Train)
classifier = GaussianNB()
classifier.fit(x_Train, y_Train)

with open('TrainedModels/trained_GaussianNB.pkl', 'wb+') as file:
    pickle.dump(classifier, file)

predictions = classifier.predict(x_Test)

print(accuracy_score(y_Test, predictions))
print(predictions)
