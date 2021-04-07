#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt


def split_date_continues():
    # Read data from csv
    data_frame = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")

    # Drop empty rows and columns
    data_frame = data_frame.dropna(how="all")
    data_frame = data_frame.dropna(axis=1, how="all")

    # Extract first column to separate dates
    col = data_frame.iloc[:, 0]
    data_frame = data_frame.drop(data_frame.columns[0], axis=1)
    col = col.str.split(expand=True)

    # Translate to English
    col.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    col["Hour"] = col["Hour"].str[0:2]

    weekdays = {
        "ma": "Mon",
        "ti": "Tue",
        "ke": "Wed",
        "to": "Thu",
        "pe": "Fri",
        "la": "Sat",
        "su": "Sun",
    }

    months = {
        "tammi": 1,
        "helmi": 2,
        "maalis": 3,
        "huhti": 4,
        "touko": 5,
        "kesä": 6,
        "heinä": 7,
        "elo": 8,
        "syys": 9,
        "loka": 10,
        "marras": 11,
        "joulu": 12,
    }

    col["Weekday"] = col["Weekday"].map(weekdays)
    col["Month"] = col["Month"].map(months)
    col = col.astype(
        {"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int}
    )

    return pd.concat([col, data_frame], axis=1)


def cyclists_per_day():
    data_frame = split_date_continues()
    data_frame = data_frame.drop(["Hour", "Weekday"], axis=1)
    new_data_frame = data_frame.groupby(["Year", "Month", "Day"]).sum()
    return new_data_frame


def main():
    data_frame = cyclists_per_day()
    data_frame_plot = data_frame.loc[(2017, 8), :]
    plt.plot(data_frame_plot)
    plt.show()


if __name__ == "__main__":
    main()
