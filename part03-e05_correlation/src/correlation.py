#!/usr/bin/env python3

import scipy.stats
import numpy as np


def load():
    # You have to import pandas inside a function for the assignment

    # Pandas is not loaded into the global memory space of Python (does not work outside this function)
    import pandas as pd

    return pd.read_csv("src/iris.csv").drop("species", axis=1).values


def lengths():
    x = load()

    # Calculate Pearson’s correlation coefficient
    return scipy.stats.pearsonr(x[:, 0], x[:, 2])[0]


def correlations():
    x = load()

    # Return Pearson product-moment correlation coefficients
    return np.corrcoef((x[:, 0], x[:, 1], x[:, 2], x[:, 3]))


def main():
    print(lengths())
    print(correlations())


if __name__ == "__main__":
    main()
