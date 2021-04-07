#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression


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


def cycling_weather_continues(station):
    # Get the splitted dates back in English
    data_frame = split_date()

    # Create a new data frame based on weekdays, hours and stations for the year 2017
    indexed_data_frame = pd.merge(
        data_frame.loc[:, "Weekday":"Hour"],
        data_frame.loc[:, station],
        left_index=True,
        right_index=True,
    )
    indexed_data_frame = indexed_data_frame[indexed_data_frame.Year == 2017]

    # Get the weather data
    weather_data_frame = pd.read_csv("src/kumpula-weather-2017.csv")

    # Merge weather and cycling data based on month and day
    final_data_frame = pd.merge(
        weather_data_frame,
        indexed_data_frame.groupby(["Month", "Day"])[station].sum(),
        right_on=["Day", "Month"],
        left_on=["d", "m"],
    )

    # Propagate last valid observation forward to next valid backfill for a NA
    final_data_frame = final_data_frame.fillna(method="ffill")

    # Perform linear regression using sklearn
    model = LinearRegression(fit_intercept=True)
    x = final_data_frame.loc[
        :, ["Precipitation amount (mm)", "Snow depth (cm)", "Air temperature (degC)"]
    ]
    y = final_data_frame.loc[:, station]
    model.fit(x, y)
    score = model.score(x, y)

    return model.coef_, score


def main():
    station = "Baana"
    coef, score = cycling_weather_continues(station)
    
    # Format print statements like this, otherwise the unit test will fail.
    print(f"Measuring station: {station}")
    print(f"Regression coefficient for variable 'precipitation': {coef[0]:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {coef[1]:.1f}")
    print(f"Regression coefficient for variable 'temperature': {coef[2]:.1f}")
    print(f"Score: {score:.2f}")


if __name__ == "__main__":
    main()
