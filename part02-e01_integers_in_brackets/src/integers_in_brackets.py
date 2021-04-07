#!/usr/bin/env python3

import re


def integers_in_brackets(s):
    # Find all ints in '[' and ']'.
    ints_in_string = re.findall(r"\[\s*([+-]?\d+)\s*\]", s)
    return list(map(int, ints_in_string))


def main():
    print(integers_in_brackets("  afd [asd] [12 ] [a34]  [ -43 ]tt [+12]xxx"))


if __name__ == "__main__":
    main()
