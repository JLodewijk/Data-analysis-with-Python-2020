#!/usr/bin/env python3

import pandas as pd


def swedish_and_foreigners():
    # Read the data
    data_frame = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)

    # Takes the subset about municipalities
    data = data_frame[1:312]

    cols = data.columns

    # Further take a subset of rows that have proportion of Swedish speaking people and proportion of foreigners both above 5 % level
    filtered = data[(data[cols[2]] > 5) & (data[cols[3]] > 5)]

    # take only columns about population, the proportions of Swedish speaking people and foreigners, that is three columns
    return filtered[[cols[0], cols[2], cols[3]]]


def main():
    print(swedish_and_foreigners())


if __name__ == "__main__":
    main()
