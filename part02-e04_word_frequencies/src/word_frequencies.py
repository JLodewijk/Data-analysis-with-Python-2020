#!/usr/bin/env python3

import re


def word_frequencies(filename):
    results = {}
    with open(filename, "r") as fp:
        for line in fp:
            
            # Match everything expect whitespaces
            regex_matches = re.findall(r"(\S*)", line)

            # Strip according to the assignment
            regex_matches = [
                match.strip("""!"#$%&'()*,-./:;?@[]_""") for match in regex_matches
            ]

            # Fill in the dictionary with counts
            for regex_match in regex_matches:
                if regex_match not in results:
                    results[regex_match] = 1
                else:
                    results[regex_match] += 1

    return results


def main():
    word_frequencies("alice.txt")


if __name__ == "__main__":
    main()
