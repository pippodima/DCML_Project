import pandas as pd

filepath = "Data/newillaoitop.csv"
filepath2 = "Data/siontopnew.csv"
df = pd.read_csv(filepath)
df['anomaly'] = 0
df2 = pd.read_csv(filepath2)
df2['anomaly'] = 0

filepath_anomaly = "Data/joriillalloi.csv"
df_anomaly = pd.read_csv(filepath_anomaly)
df_anomaly['anomaly'] = 1

combined_df = pd.concat([df, df2, df_anomaly], ignore_index=False)
combined_df.to_csv('dataset.csv', index=False)
