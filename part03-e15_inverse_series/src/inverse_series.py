#!/usr/bin/env python3

import pandas as pd


def inverse_series(serie):
    return pd.Series(serie.index.values, serie.values)


def main():
    series = pd.Series(["a", "b", "c"])
    print(inverse_series(series))


if __name__ == "__main__":
    main()
