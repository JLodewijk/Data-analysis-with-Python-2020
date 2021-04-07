#!/usr/bin/env python3

import numpy as np


def first_half_second_half(a):
    # Determine the middle_indexdle index
    middle_index = int(a.shape[1] / 2)

    # Determine if the first hald is larger than the second half.
    greater_than = np.sum(a[:, :middle_index], 1) > np.sum(a[:, middle_index:], 1)

    return a[greater_than]


def main():
    a = np.array([[1, 3, 4, 2], [2, 2, 1, 2]])
    print(first_half_second_half(a))


if __name__ == "__main__":
    main()
