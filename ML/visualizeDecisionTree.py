import numpy as np
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import export_graphviz
import graphviz as gv
import os

os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'


def calculate_mouse_distance(data):
    mouse_distances = []

    for i in range(1, len(data)):
        current_row = data.iloc[i]
        previous_row = data.iloc[i - 1]

        x_current, y_current = current_row['MOUSE_X'], current_row['MOUSE_Y']
        x_previous, y_previous = previous_row['MOUSE_X'], previous_row['MOUSE_Y']

        distance = np.sqrt((x_current - x_previous) ** 2 + (y_current - y_previous) ** 2)
        mouse_distances.append(distance)

    data['MOUSE_DISTANCE'] = [np.nan] + mouse_distances

    return data


# with x and y position mouse (0.77 accuracy)
# # df = pd.read_csv('/Users/pippodima/Documents/Uni/Magistrale/DCML/Progetto_DCML/ML/Data/dataset.csv')
df = pd.read_csv("Data/dataset.csv")
X = df[['CPU', 'MEMORY', 'MOUSE_X', 'MOUSE_Y', 'LEFT_CLICKS', 'RIGHT_CLICKS', 'q', 'w', 'e', 'r', 't', 'd', 'f', 'tab',
        'space', 'ctrl']]
Y = df['anomaly']

# with mouse distance (0.75 accuracy)
# df = calculate_mouse_distance(df)
# df.drop(['MOUSE_X', 'MOUSE_Y'], axis=1)
# X = df[['MOUSE_DISTANCE', 'LEFT_CLICKS', 'RIGHT_CLICKS', 'q', 'w', 'e', 'r', 't', 'd', 'f', 'tab', 'space', 'ctrl']]
# Y = df['anomaly']

x_Train, x_Test, y_Train, y_Test = train_test_split(X, Y, test_size=0.2, shuffle=True, random_state=42)

# classifier = DecisionTreeClassifier(min_samples_split=30, min_impurity_decrease=0.01)  # (0.74 distance vs 0.69 x,y)
classifier = DecisionTreeClassifier(max_depth=3)
# classifier = DecisionTreeClassifier()
classifier.fit(x_Test, y_Test)

dot_data = export_graphviz(classifier, out_file=None,
                           feature_names=['CPU', 'MEMORY', 'MOUSE_X', 'MOUSE_Y', 'LEFT_CLICKS', 'RIGHT_CLICKS', 'q',
                                          'w', 'e', 'r', 't', 'd', 'f', 'tab', 'space', 'ctrl'],
                           class_names=['0', '1'],
                           filled=True, rounded=True,
                           special_characters=True)

graph = gv.Source(dot_data)
graph.view()
print(accuracy_score(y_Test, classifier.predict(x_Test)))
