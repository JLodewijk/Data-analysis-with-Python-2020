#!/usr/bin/env python3

def reverse_dictionary(d):
    reverse_dict = {}
    val_list = []
    # Loop through a list of lists
    for dict_values in d.values():
        # Loop through each individual list and store the values in a new list
        for value in dict_values:
            val_list.append(value)
    # Build a new dictionary
    for value in val_list:
        temp = []
        # Get the orginal keys and values
        for i, j in d.items():
            # If current dict value is in the list, than append the key of the dict.
            if value in j:
                temp.append(i)
        reverse_dict[value] = temp
    return reverse_dict



def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))


if __name__ == "__main__":
    main()
