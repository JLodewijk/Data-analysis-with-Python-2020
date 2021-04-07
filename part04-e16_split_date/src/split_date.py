#!/usr/bin/env python3

import pandas as pd


def split_date():
    # Load the data
    data_frame = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")

    # Drop the empty entries
    data_frame = data_frame.dropna(how="all")
    data_frame = data_frame.dropna(axis=1, how="all")

    # Perform indexing of data frame
    data_frame = data_frame.iloc[:, 0]

    # Split the strings
    data_frame = data_frame.str.split(expand=True)

    # Begin converting from Finish to English
    data_frame.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    data_frame["Hour"] = data_frame["Hour"].str[0:2]

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

    data_frame = data_frame.replace(weekdays, value=None)
    data_frame = data_frame.replace(months, value=None)
    data_frame.iloc[:, 1:] = data_frame.iloc[:, 1:].astype(int)
    return data_frame


def main():
    print(split_date())


if __name__ == "__main__":
    main()
