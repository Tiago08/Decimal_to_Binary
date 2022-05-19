"""Simple program that converts binary to decimal and vice versa"""

import os
import sys

def run():
    try:
        menu = int(input("Choose an option:\n 1.Decimal to binary\n 2.Binary to decimal\nOption: "))
        if menu not in range(1,3):
            raise ValueError
        if menu == 1:
            dec = int(input("Input your decimal number: "))
            print(f"\nBinary: {bin(dec)[2:]}")
        elif menu == 2:
            binary = int(input("Input your binary number: "))
            # print(f"\nDecimal: {int(binary, 2)}")
            decimal, i, n = 0, 0, 0
            while (binary != 0):
                dec = binary % 10
                decimal = decimal + dec * pow(2, i)
                binary = binary//10
                i += 1
            print(f"Decimal: {decimal}")

    except ValueError:
        print("Choose a valid option!")

if __name__ == '__main__':
    run()
    afirmative_answer = ['y', 'Y', 'yes', 'Yes','YES', 'yeah', 'Yeah']
    while True:
        run_again = input("Run again?(y/n): ")
        if run_again in afirmative_answer:
            os.system('cls')
            run()
        else:
            sys.exit()
