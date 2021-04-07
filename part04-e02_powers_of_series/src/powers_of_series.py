#!/usr/bin/env python3

import pandas as pd


def powers_of_series(s, k):
    """
    The first column of the dataFrame should be the input Series, the second column should contain the Series raised to power of two.
    The third column should contain the Series raised to the power of three, and so on until (and including) power of k.
    """
    data_frame = pd.DataFrame(index=s.index)

    # Calculate the power for ea
    for i in range(k):
        data_frame[i + 1] = [x ** (i + 1) for x in s]
    return data_frame


def main():
    """
    Generate output like this:

         1   2   3
      a  1   1   1
      b  2   4   8
      c  3   9  27
      d  4  16  64
    """
    s = pd.Series([1, 2, 3, 4], index=list("abcd"))
    print(powers_of_series(s, 3))


if __name__ == "__main__":
    main()
