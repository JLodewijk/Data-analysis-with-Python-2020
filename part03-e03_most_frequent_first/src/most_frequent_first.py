#!/usr/bin/env python3

import numpy as np


def most_frequent_first(a, c):
    # Get the unque entries and counts
    unique_values, unique_count = np.unique(a[:, c], axis=0, return_counts=True)

    # Count all the indentical entries
    count_sorted_indentical = np.argsort(-unique_count)

    # Sort value by count
    val_sorted_by_count = unique_values[count_sorted_indentical].reshape((1, -1))

    # Get the index of array in order to sort them by most frequent first.
    indexes_of_array = np.concatenate(
        [np.where((a[:, c] == x))[0] for x in np.nditer(val_sorted_by_count)]
    )
    return a[indexes_of_array]


def main():
    a = np.array(
        [
            [5, 0, 3, 3, 7, 9, 3, 5, 2, 4],
            [7, 6, 8, 8, 1, 6, 7, 7, 8, 1],
            [5, 9, 8, 9, 4, 3, 0, 3, 5, 0],
            [2, 3, 8, 1, 3, 3, 3, 7, 0, 1],
            [9, 9, 0, 4, 7, 3, 2, 7, 2, 0],
            [0, 4, 5, 5, 6, 8, 4, 1, 4, 9],
            [8, 1, 1, 7, 9, 9, 3, 6, 7, 2],
            [0, 3, 5, 9, 4, 4, 6, 4, 4, 3],
            [4, 4, 8, 4, 3, 7, 5, 5, 0, 1],
            [5, 9, 3, 0, 5, 0, 1, 2, 4, 2],
        ]
    )
    print(most_frequent_first(a, 0))


if __name__ == "__main__":
    main()
