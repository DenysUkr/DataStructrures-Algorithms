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
            return linesCoded, linesCoded


# Purpose: Uses a binary search to find the initial lines of code to
#          write before the first cup of coffee, so that the coder
#          will complete the total lines of code before sleeping AND
#          get to have coffee as soon as possible.
# Input: total_lines - lines of code that need to be written
#        prod_loss - factor for loss of productivity after each coffee
# Output: returns the initial lines of code to write before coffee
def binary_search(total_lines: int, prod_loss: int):
    # creating an array to hold all of the possible lines of code before coffee
    numArray = [None] * total_lines
    for i in range(0, total_lines):
        numArray[i] = i + 1

    # declaring the variables for the bianary search
    low = 0
    midpoint = 0
    high = len(numArray) - 1

    iteration = 0
    # looping until find the right value
    while low <= high:

        # calculate the midpoint
        midpoint = (low + high) // 2

        if high == midpoint or sum_series(midpoint, prod_loss) == total_lines:
            return midpoint, iteration + 1
        # if the SumSeries returns a bigger number then total lines then cut off the TOP part of the array
        if sum_series(midpoint, prod_loss) > total_lines:
            high = midpoint - 1
        # if the SumSeries returns a smaller number then total lines then cut off the BOTTOM part of the array
        if sum_series(midpoint, prod_loss) < total_lines:
            low = midpoint + 1

        iteration = iteration + 1


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Open input source
    # Change debug to false before submitting
    debug = True
    if debug:
        in_data = open('work.in')
    else:
        in_data = sys.stdin

    # read number of cases
    line = in_data.readline().strip()
    num_cases = int(line)

    for i in range(num_cases):

        # read one line for one case
        line = in_data.readline().strip()
        data = line.split()
        total_lines = int(data[0])  # total number of lines of code
        prod_loss = int(data[1])  # read productivity loss factor

        print("=====> Case #", i + 1)

        # Binary Search
        start = time.time()
        print("Binary Search:")
        lines, count = binary_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        print("sum_series called", count, "times")
        finish = time.time()
        binary_time = finish - start
        print("Elapsed Time:", "{0:.8f}".format(binary_time),
              "seconds")
        print()

        # Linear Search
        start = time.time()
        print("Linear Search:")
        lines, count = linear_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        print("sum_series called", count, "times")
        finish = time.time()
        linear_time = finish - start
        print("Elapsed Time:", "{0:.8f}".format(linear_time),
              "seconds")
        print()

        # Comparison
        print("Binary Search was",
              "{0:.1f}".format(linear_time / binary_time),
              "times faster.")
        print()
        print()


if __name__ == "__main__":
    main()
