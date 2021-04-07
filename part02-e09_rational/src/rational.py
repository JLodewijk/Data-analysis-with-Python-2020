#!/usr/bin/env python3


class Rational(object):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __mul__(num1, num2):
        return Rational(
            num1.numerator * num2.numerator, num1.denominator * num2.denominator
        )

    def __truediv__(num1, num2):
        return Rational(
            num1.numerator * num2.denominator, num1.denominator * num2.numerator
        )

    def __add__(num1, num2):
        return Rational(
            num1.numerator * num2.denominator + num2.numerator * num1.denominator,
            num1.denominator * num2.denominator,
        )

    def __sub__(num1, num2):
        return Rational(
            num1.numerator * num2.denominator - num2.numerator * num1.denominator,
            num1.denominator * num2.denominator,
        )

    def __eq__(num1, num2):
        return num1.numerator == num2.numerator and num1.denominator == num2.denominator

    def __gt__(num1, num2):
        return num1.numerator * num2.denominator > num2.numerator * num1.denominator

    def __lt__(num1, num2):
        return num1.numerator * num2.denominator < num2.numerator * num1.denominator


def main():
    r1 = Rational(1, 4)
    r2 = Rational(2, 3)
    print(r1)
    print(r2)
    print(r1 * r2)
    print(r1 / r2)
    print(r1 + r2)
    print(r1 - r2)
    print(Rational(1, 2) == Rational(2, 4))
    print(Rational(1, 2) > Rational(2, 4))
    print(Rational(1, 2) < Rational(2, 4))


if __name__ == "__main__":
    main()
