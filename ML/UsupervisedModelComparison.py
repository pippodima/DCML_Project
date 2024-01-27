import pandas as pd
import numpy as np
import random

from matplotlib import pyplot as plt
from pyod.models.abod import ABOD
from pyod.models.hbos import HBOS
from sklearn.model_selection import train_test_split
from sklearn.manifold import TSNE


# Set random seed
random_seed = 42
np.random.seed(random_seed)
random.seed(random_seed)

# Load data
df = pd.read_csv('Data/dataset.csv')
X = df[['CPU', 'MEMORY', 'MOUSE_X', 'MOUSE_Y', 'LEFT_CLICKS', 'RIGHT_CLICKS', 'q', 'w', 'e', 'r', 't', 'd', 'f', 'tab',
        'space', 'ctrl']]
Y = df['anomaly']

# Split data into train and test sets
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, shuffle=True, random_state=random_seed)

# Initialize and fit ABOD model
abod = ABOD()
abod.fit(x_train)

# # Transform data using t-SNE for ABOD
# tsne_abod = TSNE(n_components=2, random_state=random_seed)
# X_tsne_abod = tsne_abod.fit_transform(x_train)
#
# # Plot clusters for ABOD
# plt.figure(figsize=(8, 6))
# plt.scatter(X_tsne_abod[:, 0], X_tsne_abod[:, 1], c=y_train, cmap='viridis')
# plt.title('t-SNE Clustering with ABOD')
# plt.xlabel('t-SNE Dimension 1')
# plt.ylabel('t-SNE Dimension 2')
# plt.colorbar(label='Anomaly')
# plt.show()

# Initialize and fit HBOS model
hbos = HBOS()
hbos.fit(x_train)

# # Transform data using t-SNE for HBOS
# tsne_hbos = TSNE(n_components=2, random_state=random_seed)
# X_tsne_hbos = tsne_hbos.fit_transform(x_train)
#
# # Plot clusters for HBOS
# plt.figure(figsize=(8, 6))
# plt.scatter(X_tsne_hbos[:, 0], X_tsne_hbos[:, 1], c=y_train, cmap='viridis')
# plt.title('t-SNE Clustering with HBOS')
# plt.xlabel('t-SNE Dimension 1')
# plt.ylabel('t-SNE Dimension 2')
# plt.colorbar(label='Anomaly')
# plt.show()


from sklearn.metrics import precision_score, recall_score, f1_score

# Predictions for ABOD
abod_pred = abod.predict(x_test)

# Precision, recall, and F1-score for ABOD
abod_precision = precision_score(y_test, abod_pred)
abod_recall = recall_score(y_test, abod_pred)
abod_f1 = f1_score(y_test, abod_pred)

print("ABOD:")
print("Precision:", abod_precision)
print("Recall:", abod_recall)
print("F1-score:", abod_f1)
print()

# Predictions for HBOS
hbos_pred = hbos.predict(x_test)

# Precision, recall, and F1-score for HBOS
hbos_precision = precision_score(y_test, hbos_pred)
hbos_recall = recall_score(y_test, hbos_pred)
hbos_f1 = f1_score(y_test, hbos_pred)

print("HBOS:")
print("Precision:", hbos_precision)
print("Recall:", hbos_recall)
print("F1-score:", hbos_f1)


# Data for plotting
models = ['ABOD', 'HBOS']
precision_scores = [abod_precision, hbos_precision]
recall_scores = [abod_recall, hbos_recall]
f1_scores = [abod_f1, hbos_f1]

# Plotting
plt.figure(figsize=(10, 6))

# Precision plot
plt.subplot(1, 3, 1)
plt.bar(models, precision_scores, color=['blue', 'orange'])
plt.title('Precision')
plt.ylim(0, 1)

# Recall plot
plt.subplot(1, 3, 2)
plt.bar(models, recall_scores, color=['blue', 'orange'])
plt.title('Recall')
plt.ylim(0, 1)

# F1-score plot
plt.subplot(1, 3, 3)
plt.bar(models, f1_scores, color=['blue', 'orange'])
plt.title('F1-score')
plt.ylim(0, 1)

plt.tight_layout()
plt.show()
