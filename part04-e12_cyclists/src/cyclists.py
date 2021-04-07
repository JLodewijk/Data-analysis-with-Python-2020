#!/usr/bin/env python3

import pandas as pd


def cyclists():
    data_frame = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")

    # Remove NA's
    data_frame_droprow = data_frame.dropna(how="all")
    data_frame_dropcol = data_frame_droprow.dropna(axis=1, how="all")

    # Return non-empty data frame
    return data_frame_dropcol


def main():
    print(cyclists())


if __name__ == "__main__":
    main()
