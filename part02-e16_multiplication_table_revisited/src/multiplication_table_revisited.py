#!/usr/bin/env python3

import numpy as np


def multiplication_table(n):
    x = np.arange(n)
    y = x.reshape(-1, 1)
    return x * y


def main():
    print(multiplication_table(4))


if __name__ == "__main__":
    main()
