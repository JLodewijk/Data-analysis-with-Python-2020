#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    # calculate the discriminant
    d = (b**2) - (4*a*c)

    # find two solutions
    sol1 = (-b-math.sqrt(d))/(2*a)
    sol2 = (-b+math.sqrt(d))/(2*a)
    return (sol1,sol2)


def main():
    print(solve_quadratic(1,2,1))

if __name__ == "__main__":
    main()
