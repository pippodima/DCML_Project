import pandas as pd
import numpy as np
import random

from matplotlib import pyplot as plt
from pyod.models.abod import ABOD
from pyod.models.hbos import HBOS
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, roc_curve
from yellowbrick.classifier import ROCAUC
from yellowbrick.features import Rank1D
from pyod.utils.data import evaluate_print



random_seed = 42
np.random.seed(random_seed)
random.seed(random_seed)

df = pd.read_csv('Data/dataset.csv')
X = df[['CPU', 'MEMORY', 'MOUSE_X', 'MOUSE_Y', 'LEFT_CLICKS', 'RIGHT_CLICKS', 'q', 'w', 'e', 'r', 't', 'd', 'f', 'tab', 'space', 'ctrl']]
Y = df['anomaly']
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, shuffle=True, random_state=random_seed)



model = ABOD()
model.fit(x_train)

# Predict Outliers on Test Set
scores_pred = model.decision_function(x_test)

# Visualize Clusters and Outliers
threshold = 0.000001  # Adjust the threshold based on outlier scores
plt.scatter(x_test['MOUSE_X'], x_test['MOUSE_Y'], color='blue', s=10, label='Inliers')
plt.scatter(x_test[scores_pred > threshold]['MOUSE_X'], x_test[scores_pred > threshold]['MOUSE_Y'],
            color='red', s=30, label='Outliers')
plt.title('ABOD Clustering with Outliers on Test Set')
plt.legend()
plt.show()
