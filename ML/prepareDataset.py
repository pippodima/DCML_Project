import pandas as pd

# replace the NORMAL-GAME and ANOMALY-GAME with your monitored games

filepath = "C:/Users/pippo/PycharmProjects/DCML_Project/ML/Data/NORMAL-GAME.csv"
filepath2 = "C:/Users/pippo/PycharmProjects/DCML_Project/ML/Data/NORMAL-GAME2.csv"
df = pd.read_csv(filepath)
df['anomaly'] = 0
df2 = pd.read_csv(filepath2)
df2['anomaly'] = 0

filepath_anomaly = "C:/Users/pippo/PycharmProjects/DCML_Project/ML/Data/ANOMALY-GAME.csv"
df_anomaly = pd.read_csv(filepath_anomaly)
df_anomaly['anomaly'] = 1

filepath_anomaly2 = "C:/Users/pippo/PycharmProjects/DCML_Project/ML/Data/ANOMALY-GAME2.csv"
df_anomaly2 = pd.read_csv(filepath_anomaly2)
df_anomaly2['anomaly'] = 1

combined_df = pd.concat([df, df_anomaly, df2, df_anomaly2], ignore_index=False)
combined_df.to_csv('dataset.csv', index=False)
