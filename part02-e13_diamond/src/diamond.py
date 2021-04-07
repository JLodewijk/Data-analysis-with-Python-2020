#!/usr/bin/env python3

import numpy as np


def diamond(n):
    # Builds the identity matrix.
    x = np.eye(n, dtype=int)

    # Uses index to get the correct pattern in the matrix and combine the results.
    x = np.concatenate([x[::-1], x[:, 1:]], axis=1)

    # Create the shape needed to pass the exercise.
    return np.concatenate([x[:-1], x[::-1]], axis=0)


def main():
    print(diamond(3))


if __name__ == "__main__":
    main()
