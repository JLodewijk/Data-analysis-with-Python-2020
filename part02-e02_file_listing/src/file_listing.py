#!/usr/bin/env python3

import re

def file_listing(filename="src/listing.txt"):
	# Create list to store regex matches
    results_regex_match = []

	# Read the filename and find the files
    with open(filename, "r") as file_content:

        for line in file_content:

            # Get the filesize, date and filename from a single line (skip empty lines)
            regex_matches = re.findall(
                r"\S+\s\d\s\w+\s\S+\s+(\d+)\s([A-Za-z]{3})\s+(\d{1,})\s(\d{2}):(\d{2})\s(.+)",
                line,
            )

            # Create a tuple and append the results
            regex_matches = (
                int(regex_matches[0][0]),
                regex_matches[0][1],
                int(regex_matches[0][2]),
                int(regex_matches[0][3]),
                int(regex_matches[0][4]),
                regex_matches[0][5],
            )
            results_regex_match.append(regex_matches)
    return results_regex_match


def main():
    print(file_listing())


if __name__ == "__main__":
    main()
