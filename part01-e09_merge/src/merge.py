#!/usr/bin/env python3


def merge(L1, L2):
    merged_list = L1 + L2
    merged_list = bubblesort(merged_list)
    return merged_list


def bubblesort(list_of_numbers):
    # Create range for iter numbers to compare elements in a  list to
    for iter_numbers in range(len(list_of_numbers) - 1, 0, -1):

        # Loop trough each an iter number range of 0 to iter_numbers.
        for i in range(iter_numbers):
            
            # If an element is larger, than move it.
            if list_of_numbers[i] > list_of_numbers[i + 1]:
                temp = list_of_numbers[i]
                list_of_numbers[i] = list_of_numbers[i + 1]
                list_of_numbers[i + 1] = temp

    return list_of_numbers


def main():
    L1 = [5, 3, 7, 1]
    L2 = [6, 1, 7, 3, 6]
    print(merge(sorted(L1), sorted(L2)))


if __name__ == "__main__":
    main()
