#!/usr/bin/env python3

import math


def main():
    # enter you solution here
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if shape == "":
            break
        elif shape == "triangle":
            base = float(input("Give base of the triangle: "))
            height = float(input("Give height of the triangle: "))
            area = 0.5 * base * height
            print("The area is " + str(area))
        elif shape == "rectangle":
            width = float(input("Give base of the triangle: "))
            height = float(input("Give height of the triangle: "))
            area = width * height
            print("The area is " + str(area))
        elif shape == "circle":
            radius = float(input("Give radius of the circle: "))
            area = str(math.pi * radius**2)
            print("The area is " + str(area))
        else:
            print("Unknown shape!")


if __name__ == "__main__":
    main()
