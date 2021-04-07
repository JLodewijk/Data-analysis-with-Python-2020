#!/usr/bin/env python3

import pandas as pd


def growing_municipalities(data_frame):
    all = data_frame.shape[0]
    cols = data_frame.columns
    filtered = data_frame[data_frame[cols[1]] > 0].index
    part = len(filtered) / all
    return part


def main():
    data_frame = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    data = data_frame[1:312]
    percentage = growing_municipalities(data) * 100
    print(percentage)
    print(f"Proportion of growing municipalities: {percentage:.1f}%")

if __name__ == "__main__":
    main()
