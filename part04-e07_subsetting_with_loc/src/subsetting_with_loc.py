#!/usr/bin/env python3

import pandas as pd


def subsetting_with_loc():
    data_frame = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    cols = data_frame.columns

    # Takes the subset of municipalities from Akaa to Äänekoski and restricts it to columns: 'Population', 'Share of Swedish-speakers of the population, %', and 'Share of foreign citizens of the population, %'.
    return data_frame.loc["Akaa":"Äänekoski"][[cols[0], cols[2], cols[3]]]


def main():
    print(subsetting_with_loc())


if __name__ == "__main__":
    main()
