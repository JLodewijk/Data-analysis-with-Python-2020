#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances
import scipy

from matplotlib import pyplot as plt

import seaborn as sns

sns.set(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc


def toint(x):
    nucleotide_to_int = {"A": 0, "C": 1, "G": 2, "T": 3}
    return nucleotide_to_int[x]


def find_permutation(n_clusters, real_labels, labels):
    """
    Permutation code given by the course
    """
    permutation = []
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label = scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation


def get_features_and_labels(filename):
    # data.seq is structured as a CSV file.
    data_frame = pd.read_csv(filename, sep="\t")

    # X: nucleotides sequence & y: label
    label = data_frame.loc[:, "y":]
    nucleotides = data_frame.loc[:, "X"].apply(lambda x: [toint(a) for a in x])
    nucleotides = np.array(nucleotides.tolist())
    return nucleotides, label


def plot(distances, method="average", affinity="euclidean"):
    # Plot the clusters
    clustering_linkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g = sns.clustermap(
        distances, row_linkage=clustering_linkage, col_linkage=clustering_linkage
    )
    g.fig.suptitle(
        "Hier. clust using {0} linkage and {1} affinity".format(method, affinity)
    )
    plt.show()


def cluster_euclidean(filename):
    features, labels = get_features_and_labels(filename)

    # Perform clustering
    clustering = AgglomerativeClustering(
        n_clusters=2, affinity="euclidean", linkage="average"
    )

    # Make predictions and test it against the retrieved labels
    predictions = clustering.fit_predict(features, labels)
    permutation = find_permutation(2, labels, predictions)
    new_labels = [permutation[label] for label in clustering.labels_]
    score = accuracy_score(labels, new_labels)

    return score


def cluster_hamming(filename):
    features, labels = get_features_and_labels(filename)

    # Perform clustering
    distance = pairwise_distances(features, metric="hamming")
    clustering = AgglomerativeClustering(
        n_clusters=2, affinity="precomputed", linkage="average"
    )

    # Make predictions and test it against the retrieved labels
    predictions = clustering.fit_predict(distance, labels)
    permutation = find_permutation(2, labels, predictions)
    new_labels = [permutation[label] for label in clustering.labels_]
    score = accuracy_score(labels, new_labels)

    return score


def main():
    print(cluster_hamming("src/data.seq"))


if __name__ == "__main__":
    main()
