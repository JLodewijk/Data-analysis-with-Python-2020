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


def suicide_weather():
    # Get weather data
    weather_data_frame = pd.read_html(
        "src/List_of_countries_by_average_yearly_temperature.html"
    )
    weather_data_frame = weather_data_frame[0]
    weather_data_frame = weather_data_frame.set_index(weather_data_frame.columns[0])
    weather_data_frame = (
        weather_data_frame.iloc[:, 0].str.replace("\u2212", "-").astype(float)
    )

    # Get suicide fractions
    suicide_fractions_data_frame = suicide_fractions()

    # Build a new data_frame
    weather_suicide_data_frame = pd.merge(
        weather_data_frame,
        suicide_fractions_data_frame,
        left_index=True,
        right_index=True,
    )
    correlation = weather_suicide_data_frame.corr(method="spearman").iloc[0, 1]
    (suicide_rows, temperature_rows, common_rows) = (
        x.shape[0]
        for x in [
            suicide_fractions_data_frame,
            weather_data_frame,
            weather_suicide_data_frame,
        ]
    )

    return suicide_rows, temperature_rows, common_rows, correlation


def main():
    suicide_rows, temperature_rows, common_rows, correlation = suicide_weather()
    print(f"Suicide DataFrame has {suicide_rows} rows")
    print(f"Temperature DataFrame has {temperature_rows} rows")
    print(f"Common DataFrame has {common_rows} rows")
    print(f"Spearman correlation: {correlation}")
    return


if __name__ == "__main__":
    main()
