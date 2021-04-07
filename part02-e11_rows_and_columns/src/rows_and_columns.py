#!/usr/bin/env python3

import numpy as np


def get_rows(number_of_rows):
    rows_list = []
    for row in number_of_rows:
        rows_list.append(row)
    return rows_list


def get_columns(number_of_columns):
    columns_list = []
    for column in number_of_columns.T:
        columns_list.append(column)
    return columns_list


def main():
    # Generate fixed random numbers
    np.random.seed(0)
    a = np.random.randint(0, 10, (4, 4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))


if __name__ == "__main__":
    main()
