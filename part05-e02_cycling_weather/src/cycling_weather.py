#!/usr/bin/env python3

import pandas as pd


def cycling_weather():
    # read the data
    data_frame_1 = pd.read_csv("src/kumpula-weather-2017.csv")

    # Call the split_data function
    data_frame_2 = split_date()

    # Create new dataframe with proper naming
    df = pd.merge(
        data_frame_1,
        data_frame_2,
        left_on=["Year", "m", "d"],
        right_on=["Year", "Month", "Day"],
    )
    columns = ["m", "d", "Time", "Time zone"]
    df.drop(columns, axis=1, inplace=True)
    return df


def split_date():
    # Read the data from CSV
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    data_frame_2 = df["Päivämäärä"].str.split(expand=True)

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
    df.drop("Päivämäärä", axis=1, inplace=True)
    df.dropna(axis=0, how="all", inplace=True)
    df.dropna(axis=1, how="all", inplace=True)
    df = pd.concat([data_frame_2, df], axis=1)

    return df


def main():
    df = cycling_weather()
    print(df.head())


if __name__ == "__main__":
    main()
