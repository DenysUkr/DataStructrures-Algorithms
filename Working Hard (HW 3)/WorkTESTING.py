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
    if lines_before_coffee//prod_loss < 1:
        return lines_before_coffee
    else:
        return sum_series(lines_before_coffee//prod_loss, prod_loss) + lines_before_coffee


# Purpose: Uses a linear search to find the initial lines of code to
#          write before the first cup of coffee, so that the coder
#          will complete the total lines of code before sleeping AND
#          get to have coffee as soon as possible.
# Input: total_lines - lines of code that need to be written
#        prod_loss - factor for loss of productivity after each coffee
# Output: returns the initial lines of code to write before coffee
def linear_search(total_lines, prod_loss):
    for linesCoded in range(total_lines):
        if sum_series(linesCoded, prod_loss) >= total_lines:
            return linesCoded, linesCoded


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
    high = total_lines

    iteration = 0
    # looping until find the right value
    while low <= high:
        print(f"Itterration #{iteration+1}")

        # calculate the midpoint
        midpoint = (low + high)//2
        print(f"Midpoint = {midpoint}")
        print(f"sum_series({midpoint}, {prod_loss}) = {sum_series(midpoint,prod_loss)} vs {total_lines}")


        if high == midpoint or sum_series(midpoint, prod_loss) == total_lines :
            print(f"Returning Midpoint at {midpoint}")
            print(f"Returning {iteration+1} ")
            return midpoint, iteration + 1
        # if the SumSeries returns a bigger number then total lines then cut off the TOP part of the array
        if sum_series(midpoint, prod_loss) > total_lines:
            print(f"Our bounds are: {low} to {high}")
            print(f"Replacing high({high}) with mid({midpoint})")
            high = midpoint - 1
        # if the SumSeries returns a smaller number then total lines then cut off the BOTTOM part of the array
        if sum_series(midpoint, prod_loss) < total_lines:
            print(f"Our bounds are: {low} to {high}")
            print(f"Replacing low({low}) with mid({midpoint})")
            low = midpoint + 1

        iteration = iteration + 1
        print("__________________________________________________")


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():
    linesOfCode = 100000
    productivityDrop = 7
    print(f" Lines of code are: {linesOfCode} "
          f"\n Productivity Drop is: {productivityDrop} "
          f"\n Our sum is: {sum_series(linesOfCode, productivityDrop)}")
    print(f" TEST : {sum_series(77784, 7)}")

    print(f"Linear Search Output = {linear_search(linesOfCode, productivityDrop)}")
    binary_search(linesOfCode, productivityDrop)


if __name__ == "__main__":
    main()
