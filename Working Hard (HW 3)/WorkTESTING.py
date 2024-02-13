#  File: Work.py
#  Student Name: DENYS OSMAK
#  Student UT EID: DO7369
#  Partner Name: Michael-Aidan Suarez
#  Partner UT EID: Mjs7275

import sys
import time


# Purpose: Determines how many lines of code will be written
#          before the coder crashes to sleep. Must be implemented
#          using recursion.
# Input: lines_before_coffee - how many lines of code to write before coffee
#        prod_loss - factor for loss of productivity after coffee
# Output: returns the number of lines of code that will be written
#         before the coder falls asleep
def sum_series(lines_before_coffee, prod_loss):
    if lines_before_coffee//prod_loss == 0:
        return lines_before_coffee
    else:
        return sum_series(lines_before_coffee, prod_loss * 2) + lines_before_coffee // prod_loss


# Purpose: Uses a linear search to find the initial lines of code to
#          write before the first cup of coffee, so that the coder
#          will complete the total lines of code before sleeping AND
#          get to have coffee as soon as possible.
# Input: total_lines - lines of code that need to be written
#        prod_loss - factor for loss of productivity after each coffee
# Output: returns the initial lines of code to write before coffee
def linear_search(total_lines, prod_loss):
    for linesCoded in range(1, total_lines):
        if sum_series(linesCoded, prod_loss) >= total_lines:
            return linesCoded


# Purpose: Uses a binary search to find the initial lines of code to
#          write before the first cup of coffee, so that the coder
#          will complete the total lines of code before sleeping AND
#          get to have coffee as soon as possible.
# Input: total_lines - lines of code that need to be written
#        prod_loss - factor for loss of productivity after each coffee
# Output: returns the initial lines of code to write before coffee
def binary_search(total_lines, prod_loss):
    # creating an array to hold all of the possible lines of code before coffee
    numArray = [None] * total_lines
    for i in range(0, total_lines):
        numArray[i] = i+1

    # declaring the variables for the bianary search
    low = 0
    midpoint = 0
    high = len(numArray) - 1

    iteration = 1
    # looping until find the right value
    while low <= high:
        print(f"Itterration #{iteration}")

        # calculate the midpoint
        midpoint = (low + high)//2
        print(f"Midpoint = {iteration}")


        if high == midpoint or sum_series(midpoint, prod_loss) == total_lines :
            print(f"Returning Midpoint at {midpoint}")
            return midpoint
        # if the SumSeries returns a bigger number then total lines then cut off the TOP part of the array
        if sum_series(midpoint, prod_loss) > total_lines:
            print(f"Replacing high({high}) with mid({midpoint})")
            high = midpoint - 1
        # if the SumSeries returns a smaller number then total lines then cut off the BOTTOM part of the array
        if sum_series(midpoint, prod_loss) < total_lines:
            print(f"Replacing low({low}) with mid({midpoint})")
            low = midpoint + 1

        iteration = iteration + 1
        print("__________________________________________________")


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():
    print(f" Our sum is: {sum_series(20, 2)}")
    binary_search(300, 2)


if __name__ == "__main__":
    main()
