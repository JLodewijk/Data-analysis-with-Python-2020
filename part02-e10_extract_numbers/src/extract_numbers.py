#!/usr/bin/env python3

def extract_numbers(s):
    extracted_numbers = []
    splitted_string = s.split()
    for word in splitted_string:

        # First try converting into int, if error then:
        try:
            extracted_numbers.append(int(word))
        except:

            # Convert to float, else pass the error (assignment needs a pass for unit testing).
            try:
                extracted_numbers.append(float(word))
            except:
                pass

    return extracted_numbers

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
