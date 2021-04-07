#!/usr/bin/env python3

import sys
import re
import math


def summary(filename):
    with open(filename, "r") as file:
        summary_file = file.read()

        # Find the numeric values into a file
        regex_matches = re.findall(r"([+|-]*\d+.?\d*)", summary_file)

        # Convert to floats to calculate the total, average and standard deviation.
        numbers_in_list = [float(i) for i in regex_matches]
        l = len(numbers_in_list)
        total = sum(numbers_in_list)
        avg = total / l
        temp = [(i - avg) ** 2 for i in numbers_in_list]
        std = math.sqrt(sum(temp) / (l - 1))
    return (total, avg, std)


def main():
    for x in sys.argv[1:]:
        total, avg, std = summary(x)
        print(f"File: {x} Sum: {total:.6f} Average: {avg:.6f} Stddev: {std:.6f}")


if __name__ == "__main__":
    main()
