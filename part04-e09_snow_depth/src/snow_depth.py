#!/usr/bin/env python3

import pandas as pd


def snow_depth():
    data_frame = pd.read_csv("src/kumpula-weather-2017.csv")
    return data_frame.describe()["Snow depth (cm)"]["max"]


def main():
    max_snow_depth = snow_depth()
    print(f"Max snow depth: {max_snow_depth}")


if __name__ == "__main__":
    main()
