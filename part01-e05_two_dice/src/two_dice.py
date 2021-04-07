#!/usr/bin/env python3

def main():
    for dice_1 in range(1,7):
        for dice_2 in range(1,7):
            sum_of_dices = dice_1 + dice_2
            if sum_of_dices == 5:
                print("("+str(dice_1)+","+str(dice_2)+")")

if __name__ == "__main__":
    main()
