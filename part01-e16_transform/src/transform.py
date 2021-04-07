#!/usr/bin/env python3


def transform(s1, s2):
    transformed_values = []

    # Split and convert to int
    l1 = s1.split()
    l1 = map(int, l1)
    l2 = s2.split()
    l2 = map(int, l2)
    
    # Loop and multiply the values
    for value_1, value_2 in zip(l1, l2):
        transformed_values.append(value_1 * value_2)

    return transformed_values


def main():
    print(transform("1 5 3", "2 6 -1"))


if __name__ == "__main__":
    main()
