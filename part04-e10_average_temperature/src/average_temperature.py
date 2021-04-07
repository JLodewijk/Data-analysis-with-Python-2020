#!/usr/bin/env python3

import pandas as pd


def average_temperature():
    data_frame = pd.read_csv("src/kumpula-weather-2017.csv")
    
    # Get the data from the month of July.
    data_frame_july = data_frame[data_frame.m == 7]

    # Get the average temperature.
    return data_frame_july.describe().iloc[1, -1]


def main():
    print(f"Average temperature in July: {average_temperature()}")


if __name__ == "__main__":
    main()
