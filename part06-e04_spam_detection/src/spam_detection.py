#!/usr/bin/env python3

import gzip
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


def spam_detection(random_state=0, fraction=1.0):
    # Open gzips
    with gzip.open("src/spam.txt.gz", "rb") as f:
        file_content = f.readlines()
    spam = file_content[: int(0.1 * len(file_content))]
    with gzip.open("src/ham.txt.gz", "rb") as f:
        file_content = f.readlines()
    ham = file_content[: int(0.1 * len(file_content))]

    # Converts messages in form of text strings to feature vectors
    x = ham + spam
    vectorizer = CountVectorizer()
    x = vectorizer.fit_transform(x).toarray()

    y = np.zeros(len(x))
    y[len(ham) :] = 1

    # Create test and training datasets
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, random_state=random_state, train_size=0.75
    )

    # Create a model 
    model = MultinomialNB()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    score = accuracy_score(y_test, y_pred)
    miss = int((1 - score) * (len(y_pred)))
    return score, len(x_test), miss


def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")


if __name__ == "__main__":
    main()
