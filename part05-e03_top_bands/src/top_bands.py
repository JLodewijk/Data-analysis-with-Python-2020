#!/usr/bin/env python3

import pandas as pd


def top_bands():
    # Read the data of top 40 and bands
    top = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    bands = pd.read_csv("src/bands.tsv", sep="\t")

    # Convert to uppercase for proper sorting
    bands["Band"] = bands["Band"].str.upper()

    # Merge the data into a single dataframe
    return pd.merge(top, bands, left_on=["Artist"], right_on=["Band"])


def main():
    print(top_bands())


if __name__ == "__main__":
    main()
