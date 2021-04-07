#!/usr/bin/env python3

import pandas as pd


def below_zero():
    data_frame = pd.read_csv("src/kumpula-weather-2017.csv")
    data_frame_below_zero = data_frame[data_frame["Air temperature (degC)"] < 0]
    return len(data_frame_below_zero.index)


def main():
    print(f"Number of days below zero: {below_zero()}")


if __name__ == "__main__":
    main()
