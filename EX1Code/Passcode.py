# File: Passcode.py
# Description: Given a sequence of number, find length traveled on number pad
# Student Name: 
# Student UT EID: 
# Course Name:

import math
import sys


# Input: a list of integers representing the sequence of numbers in a password, 
# len(ptrn) >= 2
# Output: distance traveled on the number pad
def get_distance(pattern):
    output = 0

    for num in range(len(pattern)-1):
        # finding the distances between
        num1 = find_in_keypad(pattern[num])
        num2 = find_in_keypad(pattern[num+1])

        # finding the a & b in pathogen therm
        rowDif = pow(num1[0] - num2[0], 2)
        colDif = pow(num1[1] - num2[1], 2)
        distance = pow(rowDif + colDif, 0.5) # finding the square root by power of 1/2
        output += distance
    return output



# DO NOT Edit Below This Line, except for changing the debug variable when you are done


#  Find the equivilant x,y based on grid concept
def find_in_keypad (num):
    row = (num - 1) // 4
    col = (num - 1) % 4
    return (row, col)

# take an inpuyt string and create a list of numbers
def get_pattern (line):
    input_pattern = []
    line = line.split()
    for element in line:
        input_pattern.append(int(element))
    return input_pattern
    
# run the program
def main():
    
    # open file
    debug = False
    if debug:
        in_data = open('passcode.in')
    else:
        in_data = sys.stdin

    # read and process each line until EOF
    line = in_data.readline()
    while line != "":
        pattern = get_pattern(line)
        print(f'Pattern: {pattern}')
        print("Distance: {:.2f}".format(get_distance(pattern)))
        print()
        line = in_data.readline()

if __name__ == "__main__":
    main()