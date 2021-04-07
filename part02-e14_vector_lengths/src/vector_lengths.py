#!/usr/bin/env python3

import numpy as np

def vector_lengths(a):
    return np.sqrt(np.sum(np.square(a), axis=1))


def main():
    a = np.array([[5, 0, 3], [3, 7, 9]])
    print(vector_lengths(a))


if __name__ == "__main__":
    main()
