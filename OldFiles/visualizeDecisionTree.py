from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import export_graphviz
import graphviz as gv

df = pd.read_csv('/Users/pippodima/Documents/Uni/Magistrale/DCML/Progetto_DCML/ML/Data/dataset.csv')
X = df[['CPU', 'MEMORY', 'MOUSE_X', 'MOUSE_Y', 'LEFT_CLICKS', 'RIGHT_CLICKS', 'q', 'w', 'e', 'r', 't', 'd', 'f', 'tab', 'space', 'ctrl']]
Y = df['anomaly']
x_Train, x_Test, y_Train, y_Test = train_test_split(X, Y, test_size=0.2, shuffle=True, random_state=42)


classifier = DecisionTreeClassifier(min_samples_split=30, min_impurity_decrease=0.01)
# classifier = DecisionTreeClassifier()
classifier.fit(x_Test, y_Test)


# Export the decision tree to DOT format
dot_data = export_graphviz(classifier, out_file=None,
                           feature_names=['CPU', 'MEMORY', 'MOUSE_X', 'MOUSE_Y', 'LEFT_CLICKS', 'RIGHT_CLICKS', 'q', 'w', 'e', 'r', 't', 'd', 'f', 'tab', 'space', 'ctrl'],
                           class_names=['0', '1'],
                           filled=True, rounded=True,
                           special_characters=True)

# Create a graph from DOT datax     x
graph = gv.Source(dot_data)

# Save the graph to a file (optional)
graph.render("decision_tree")

# Display the decision tree
graph.view()
print(accuracy_score(y_Test, classifier.predict(x_Test)))
