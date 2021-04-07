#!/usr/bin/env python3

import pandas as pd
import numpy as np


def last_week():
    # Read the data
    data_frame = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")

    # Start reconstruct the top40 list of the previous week based on this week list
    data_frame["WoC"] -= 1

    # Use last week data of the top 40 get known where the song previously stood.
    data_frame = data_frame[~data_frame["LW"].isin(["New", "Re"])]
    data_frame["LW"] = data_frame["LW"].astype(int)

    # Determine which numeric positions we can ignore using masks 
    mask1 = data_frame["Peak Pos"] == data_frame["Pos"]
    mask2 = data_frame["Pos"] < data_frame["LW"]
    mask = mask1 & mask2
    data_frame.loc[mask, "Peak Pos"] = np.nan
    data_frame = data_frame.sort_values(by=["LW"])
    data_frame.index = data_frame["LW"]
    data_frame = data_frame.reindex(range(1, 41))
    data_frame["Pos"] = data_frame.index
    data_frame["LW"] = np.nan
    return data_frame


def main():
    data_frame = last_week()
    print("Shape: {}, {}".format(*data_frame.shape))
    print("dtypes:", data_frame.dtypes)
    print(data_frame)


if __name__ == "__main__":
    main()
