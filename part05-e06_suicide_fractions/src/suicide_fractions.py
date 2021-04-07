#!/usr/bin/env python3

import pandas as pd


def suicide_fractions():
    # Read the CSV file
    data_frame = pd.read_csv("src/who_suicide_statistics.csv")

    # Calculation the fraction
    data_frame["suicide_ratio"] = data_frame["suicides_no"] / data_frame["population"]

    # Group by country
    data_frame = data_frame.groupby("country")

    return data_frame["suicide_ratio"].mean()


def main():
    suicide_fractions()


if __name__ == "__main__":
    main()
