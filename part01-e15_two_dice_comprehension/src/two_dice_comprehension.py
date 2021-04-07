#!/usr/bin/env python3

def main():
    dices = [(i,x) for i in range(1,7) for x in range(1,7) if i+x == 5]
    for dice in dices:
        print(dice)

if __name__ == "__main__":
    main()
