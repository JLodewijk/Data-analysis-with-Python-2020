#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt


def split_date():
    # Read the data from CSV
    data_frame = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    data_frame_2 = data_frame["Päivämäärä"].str.split(expand=True)

    # Drop empty rows and columns
    data_frame_2.dropna(inplace=True)
    data_frame_2.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    data_frame_2["Hour"] = data_frame_2["Hour"].str.split(":", expand=True)[0]

    # Translate Finish to English
    days = dict(
        zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split())
    )
    months = dict(
        zip(
            "tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(),
            range(1, 13),
        )
    )

    # Insert the English data into a dataframe
    data_frame_2["Weekday"] = data_frame_2["Weekday"].map(days)
    data_frame_2["Month"] = data_frame_2["Month"].map(months)

    # Define the data types present in each column
    data_frame_2 = data_frame_2.astype(
        {"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int}
    )

    # Dropping unecessary rows and columns in data_frame
    data_frame.drop("Päivämäärä", axis=1, inplace=True)
    data_frame.dropna(axis=0, how="all", inplace=True)
    data_frame.dropna(axis=1, how="all", inplace=True)
    data_frame = pd.concat([data_frame_2, data_frame], axis=1)

    return data_frame


def commute():
    # Split the date
    data_frame = split_date()
    data_frame["Date"] = pd.to_datetime(
        data_frame[["Day", "Month", "Year", "Hour"]], dayfirst=True
    )
    data_frame = data_frame.drop(["Day", "Month", "Year", "Hour", "Weekday"], axis=1)
    data_frame = data_frame.set_index("Date")

    # Select the data
    data_frame = data_frame["2017-08-01":"2017-08-31"]
    data_frame["Weekday"] = data_frame.index.weekday
    data_frame["Weekday"] = data_frame["Weekday"] + 1
    data_frame = data_frame.groupby("Weekday").sum()
    print(data_frame)
    return data_frame


def main():
    data_frame = commute()
    plt.plot(data_frame)
    plt.show()


if __name__ == "__main__":
    main()
