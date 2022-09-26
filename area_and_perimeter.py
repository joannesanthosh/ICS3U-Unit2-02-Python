#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Sept 2022
# This is the Area and Perimeter program for rectangles

import math


def main():
    # This function calculates the area and perimeter

    # input
    length_of_rectangle = int(input("Enter the length of the rectangle (cm): "))
    width_of_rectangle = int(input("Enter the width of the rectangle (cm): "))

    # process
    area_of_rectangle = length_of_rectangle * width_of_rectangle
    perimeter_of_rectangle = 2 * (length_of_rectangle + width_of_rectangle)

    # output
    print("")
    print("The area is {0} mm².".format(area_of_rectangle))
    print("The perimeter is {0} mm.".format(perimeter_of_rectangle))

    print("\nDone.")


if __name__ == "__main__":
    main()
