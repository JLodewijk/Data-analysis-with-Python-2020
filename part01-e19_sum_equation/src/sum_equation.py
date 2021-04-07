#!/usr/bin/env python3


def sum_equation(L):
    # if empty list return "0 = 0"
    if not L:
        return "0 = 0"
    else:
        # Convert all the ints from a list into a list containing strings.
        string_sum = [str(int) for int in L]

        # Create a sum as a string.
        string_sum = " + ".join(string_sum)

        # Calculate the actual sum and insert it after the '=' sign.
        return string_sum + " = " + str(sum(L))


def main():
    print(sum_equation([1, 5, 7]))
    print(sum_equation([]))


if __name__ == "__main__":
    main()
