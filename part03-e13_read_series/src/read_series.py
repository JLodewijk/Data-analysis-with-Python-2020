#!/usr/bin/env python3

import pandas as pd


def read_series():
    indexes = []
    values = []
    while True:
        data = input("Enter data: ")
        if len(data) == 0:
            break
        else:
            splitted = data.split()
            if len(splitted) < 2:
                raise Exception
            else:
                indexes.append(splitted[0])
                values.append("".join(splitted[1:]))

    return pd.Series(values, indexes)


def main():
    read_series()


if __name__ == "__main__":
    main()
