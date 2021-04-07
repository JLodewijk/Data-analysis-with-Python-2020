#!/usr/bin/env python3

import pandas as pd


def best_record_company():
    # read data
    top = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")

    # Group by publisher
    top_by_pub = top.groupby("Publisher")

    # Sort by how long a song is on the chart
    weeks_on_chart = top_by_pub["WoC"].sum()
    weeks_on_chart = weeks_on_chart.sort_values(ascending=False)

    # Get the best pub based on WoC
    top_publisher = weeks_on_chart.index[0]
    return top[top.Publisher == top_publisher]


def main():
    print(best_record_company())


if __name__ == "__main__":
    main()
