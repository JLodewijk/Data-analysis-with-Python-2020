#!/usr/bin/env python3

import pandas as pd


def special_missing_values():
    """
    Read the data set of the top forty singles from the beginning of the year 1964 from the src folder.

    Return the rows whose singles’ position dropped compared to last week’s position (column LW=Last Week).
    """
    data_frame = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    existing = data_frame[~data_frame["LW"].isin(["New", "Re"])]
    dropped = existing[existing["Pos"] > existing["LW"].astype(int)]
    return dropped


def main():
    print(special_missing_values())


if __name__ == "__main__":
    main()
