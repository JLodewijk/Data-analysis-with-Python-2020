#!/usr/bin/env python3

def find_matching(L, pattern):
    return [i for i, e in enumerate(L) if pattern in e]

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
