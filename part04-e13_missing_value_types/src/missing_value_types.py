#!/usr/bin/env python3

import pandas as pd
import numpy as np


def missing_value_types():
    # Generate data frame with None types for missing values (values recieved from the assignemnt description)
    countries = ["United Kingdom", "Finland", "USA", "Sweden", "Germany", "Russia"]
    year_of_inpedence = [None, 1917, 1776, 1523, None, 1992]
    presidents = [None, "Niinistö", "Trump", None, "Steinmeier", "Putin"]

    data_frame = pd.DataFrame(
        {
            "State": countries,
            "Year of independence": year_of_inpedence,
            "President": presidents,
        }
    ).set_index("State")

    return data_frame


def main():
    missing_value_types()


if __name__ == "__main__":
    main()
