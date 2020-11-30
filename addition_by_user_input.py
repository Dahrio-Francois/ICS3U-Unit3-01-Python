#!/usr/bin/env python 3
#
# Created by: Dahrio Francois
# Created on: Novemeber 2020
# this program takes two numbers and adds them together
#     with user input


def main():
    # this function calculates two numbers and adds them together

    # input
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    # process
    addition = number1 + number2

    # output
    print("")
    print("the two numbers added = {}".format(addition))


if __name__ == "__main__":
    main()
