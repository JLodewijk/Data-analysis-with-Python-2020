#!/usr/bin/env python3

def triple(number):
    return number * 3

def square(number):
    return number ** 2

def main():
    for i in range(1, 11):
        tripple_value = triple(i)
        square_value = square(i)
        if square_value > tripple_value:
            break
        print("triple(" + str(i) +")==" + str(tripple_value) + " square(" + str(i) +")==" + str(square_value) )

if __name__ == "__main__":
    main()
