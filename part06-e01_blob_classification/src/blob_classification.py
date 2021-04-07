#!/usr/bin/env python3

import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn import datasets
from sklearn.model_selection import train_test_split


def blob_classification(X, y):
    """
    X: Matrix containing the data
    y: contains the labels that define different states
    """
    # Split the data into training and test datasets
    x_train, x_test, y_train, y_test = train_test_split(
        X, y, random_state=0, train_size=0.75
    )
    # Train the model
    model = GaussianNB()
    model.fit(x_train, y_train)

    # Perform predictions using the trained model
    y_predicted = model.predict(x_test)

    # Calculate the prediction accuracy score
    return metrics.accuracy_score(y_test, y_predicted)


def main():
    # Generate dataset
    X, y = datasets.make_blobs(100, 2, centers=2, random_state=2, cluster_std=2.5)

    # Perform classification and see the score
    print("The accuracy score is", blob_classification(X, y))

    # Assignment given test code
    a = np.array(
        [[2, 2, 0, 2.5], [2, 3, 1, 1.5], [2, 2, 6, 3.5], [2, 2, 3, 1.2], [2, 4, 4, 2.7]]
    )
    accs = []
    for row in a:
        X, y = datasets.make_blobs(
            100,
            int(row[0]),
            centers=int(row[1]),
            random_state=int(row[2]),
            cluster_std=row[3],
        )
        accs.append(blob_classification(X, y))
    print(repr(np.hstack([a, np.array(accs)[:, np.newaxis]])))


if __name__ == "__main__":
    main()
