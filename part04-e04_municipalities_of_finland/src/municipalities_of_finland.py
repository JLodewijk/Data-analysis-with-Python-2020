#!/usr/bin/env python3

import pandas as pd


def municipalities_of_finland():
    data_frame = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    
    # Return only the first until 312 municipalities of finland
    return data_frame[1:312]


def main():
    print(municipalities_of_finland())


if __name__ == "__main__":
    main()
