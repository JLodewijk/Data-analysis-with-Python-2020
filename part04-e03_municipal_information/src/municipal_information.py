#!/usr/bin/env python3

import pandas as pd


def main():
    # Read data
    data_frame = pd.read_csv("src/municipal.tsv", sep="\t")

    # Get the data into a particular format
    print(f"Shape: {data_frame.shape[0]},{data_frame.shape[1]}")
    
    # Print columns of the data frame
    print("Columns:")
    for x in data_frame.columns:
        print(x)


if __name__ == "__main__":
    main()
