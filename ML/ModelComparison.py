import os
import pickle
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from yellowbrick.classifier import ClassificationReport


save_img = False
show_img = False
save_models = True
names = ['RandomForest', 'KNeighbors', 'GaussianNB', 'LinearDiscriminantAnalysis', 'LogisticRegression', 'MultiLayerPerceptron']
save_path_img = 'C:/Users/pippo/PycharmProjects/DCML_Project/Images/All'
save_path_models = 'C:/Users/pippo/PycharmProjects/DCML_Project/ML/TrainedModels'
classifiers = [RandomForestClassifier(), KNeighborsClassifier(), GaussianNB(), LinearDiscriminantAnalysis(), LogisticRegression(), MLPClassifier()]
predictions = []
reports = []


df = pd.read_csv('Data/dataset.csv')
X = df[['CPU', 'MEMORY', 'MOUSE_X', 'MOUSE_Y', 'LEFT_CLICKS', 'RIGHT_CLICKS', 'q', 'w', 'e', 'r', 't', 'd', 'f', 'tab', 'space', 'ctrl']]
Y = df[['anomaly']]
x_Train, x_Test, y_Train, y_Test = train_test_split(X, Y, test_size=0.2, shuffle=True)

for classifier in classifiers:
    classifier.fit(x_Train, y_Train)

for classifier in classifiers:
    predictions.append(classifier.predict(x_Test))

for prediction in predictions:
    print(classification_report(y_Test, prediction))
    reports.append(classification_report(y_Test, prediction))

if show_img:
    for i, classifier in enumerate(classifiers):
        visualizer = ClassificationReport(classifier, support=True)
        visualizer.score(x_Test, y_Test)
        if save_img:
            os.makedirs(os.path.dirname(f'{save_path_img}/{names[i]}.png'), exist_ok=True)
            plt.savefig(f'{save_path_img}/{names[i]}.png', bbox_inches='tight')
        visualizer.show()

if save_models:
    for i, classifier in enumerate(classifiers):
        with open(f'{save_path_models}/{names[i]}.pkl', 'wb+') as model_file:
            pickle.dump(classifier, model_file)