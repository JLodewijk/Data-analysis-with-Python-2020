#!/usr/bin/env python3

import pandas as pd
import numpy as np
import scipy
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score


def find_permutation(number_of_clusters, real_labels, labels):
    permutation = []
    for i in range(number_of_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label = scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation


def nonconvex_clusters():
    # Load the data and get the features and labels
    data_frame = pd.read_csv("src/data.tsv", sep="\t")
    features = data_frame.loc[:, ["X1", "X2"]]
    labels = data_frame.iloc[:, -1]
    lab_len = len(set(labels))
    reslist = []

    # Use different distances for each cluster
    for i in np.arange(0.05, 0.2, 0.05):
        model = DBSCAN(eps=i)
        model.fit(features)
        outliners = 0

        # Number of clusters
        number_of_clusters = len(set(model.labels_))

        # Correct for outliers by chaning the number of clusters
        if -1 in model.labels_:
            number_of_clusters -= 1
            outliners = list(model.labels_).count(-1)

        permutation = find_permutation(number_of_clusters, labels, model.labels_)
        new_labels = pd.DataFrame([permutation[label] for label in model.labels_]).iloc[
            :, 0
        ]
        non_outliers_mask = model.labels_ == -1

        # Calculate score only if the number of labels is the same as the number_of_clusters
        if lab_len != number_of_clusters:
            score = None
        else:
            score = accuracy_score(
                labels[~non_outliers_mask], new_labels[~non_outliers_mask]
            )

        reslist.append([i, score, number_of_clusters, outliners])

    data_frame = pd.DataFrame(
        reslist, columns=["eps", "Score", "Clusters", "Outliers"], dtype=float
    )
    return data_frame


def main():
    print(nonconvex_clusters())


if __name__ == "__main__":
    main()
