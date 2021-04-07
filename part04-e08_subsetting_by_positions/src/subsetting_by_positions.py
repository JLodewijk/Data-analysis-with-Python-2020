#!/usr/bin/env python3

import pandas as pd


def subsetting_by_positions():
    data_frame = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t", index_col=0)

    # Return the top 10 entries and only the columns Title and Artist
    return data_frame.iloc[:10][["Title", "Artist"]]


def main():
    subsetting_by_positions()


if __name__ == "__main__":
    main()
