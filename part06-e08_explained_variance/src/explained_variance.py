#!/usr/bin/env python3

import pandas as pd
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt


def explained_variance():
    data_frame = pd.read_csv("src/data.tsv", sep="\t")
    var = data_frame.var(axis=0)
    pca = PCA()
    pca.fit(data_frame)
    return var, pca.explained_variance_


def main():
    v, ev = explained_variance()
    print(sum(v), sum(ev))

    # The variance should be printed with precision of three decimals!
    v_str_list = " ".join([f"{x:.3f}" for x in v])
    ev_str_list = " ".join([f"{x:.3f}" for x in ev])

    print("The variances are: {}".format(v_str_list))
    print("The explained variances after PCA are: {}".format(ev_str_list))

    plt.plot(np.arange(1, 11), np.cumsum(ev))
    plt.show()


if __name__ == "__main__":
    main()
