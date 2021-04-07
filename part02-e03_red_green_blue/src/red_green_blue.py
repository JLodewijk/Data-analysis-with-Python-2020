#!/usr/bin/env python3

import re


def red_green_blue(filename="src/rgb.txt"):
    results = []
    with open(filename, "r") as fp:
        # Skip first line.
        next(fp)

        # Start at the second line.
        for line in fp:
            
            # This solution is not allowed according to the unit test
            # line = re.sub(r"\s+", "\t", line)
            # results.append(line)

            # Therefore do this long solution.
            regex_pattern = (
                r"(\s*\d{1,3})\s+(\d{1,3})\s+(\d{1,3})\s+(.+)"  # (\w+|\w+\s+\w+)
            )
            regex_matches = re.match(regex_pattern, line)
            regex_matches = regex_matches.groups()
            regex_matches = f"{regex_matches[0]}\t{regex_matches[1]}\t{regex_matches[2]}\t{regex_matches[3]}"
            results.append(regex_matches)

    return results


def main():
    print(red_green_blue(filename="rgb.txt"))


if __name__ == "__main__":
    main()
