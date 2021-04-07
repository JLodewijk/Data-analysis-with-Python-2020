#!/usr/bin/env python3

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn import metrics


def plant_classification():
    # Get the iris dataset
    iris_data = load_iris()

    # Get the data and the labels
    x, y = iris_data.data, iris_data.target

    # Split the dataset into training and test
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=0
    )

    # Train the model
    model = naive_bayes.GaussianNB()
    model.fit(x_train, y_train)
    y_fitted = model.predict(x_test)

    # Return arracy score
    return metrics.accuracy_score(y_test, y_fitted)


def main():
    print("The accuracy score is", plant_classification())


if __name__ == "__main__":
    main()