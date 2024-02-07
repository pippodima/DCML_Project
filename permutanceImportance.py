import pickle

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.inspection import permutation_importance
import pandas as pd


def plot_permutation_importance(clf, X, y, ax):
    result = permutation_importance(clf, X, y, n_repeats=30, random_state=42, n_jobs=-1)
    perm_sorted_idx = result.importances_mean.argsort()

    ax.boxplot(
        result.importances[perm_sorted_idx].T,
        vert=False,
        labels=X.columns[perm_sorted_idx],
    )
    ax.axvline(x=0, color="k", linestyle="--")
    return ax


if __name__ == '__main__':
    df = pd.read_csv('ML/Data/dataset.csv')
    X = df[
        ['CPU', 'MEMORY', 'MOUSE_X', 'MOUSE_Y', 'LEFT_CLICKS', 'RIGHT_CLICKS', 'q', 'w', 'e', 'r', 't', 'd', 'f', 'tab',
         'space', 'ctrl']]
    Y = df['anomaly']
    x_Train, x_Test, y_Train, y_Test = train_test_split(X, Y, test_size=0.2, shuffle=True, random_state=42)

    with open('ML/TrainedModels/RandomForest.pkl', 'rb') as file:
        classifier = pickle.load(file)
        fig, ax = plt.subplots(1, 1)
        ax = plot_permutation_importance(classifier, x_Train, y_Train, ax)
        plt.show()


