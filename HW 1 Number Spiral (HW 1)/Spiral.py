#  File: Spiral.py
#  Student Name: Denys Osmak
#  Student UT EID: do7369

import sys

# Input: in_data - handle to the input file
# Output: integer size of the spiral, odd integer between 1 and 100
def get_dimension(in_data):

    for line in in_data:
        try:
            if not(isinstance(int(line), int)) or int(line) > 99 or int(line) < 1:
                print("Invalid spiral size")
                sys.exit(-1)
            else:
                return int(line)
        except ValueError:
            print("Invalid spiral size")
        
    


# Input: n - size of spiral
# Output: returns a 2-D list representing a spiral
def create_spiral(n):

    #in case n is null or empty
    if not isinstance(n, int):
        return [[]]

    # 	Find and set the center piece & set to 1
    center = int(n / 2)
    spiral = [[0 for i in range(n)] for i in range(n)]
    spiral[center][center] = 1
    numOfSpirals = center
    # checking edge case if the size is eqaual to 1
    if center == 0:
        return spiral

    # 	2. Create a tep variable to hold the position of where the next spiral stasrts
    # 		a. The first spiral starts on the same y level but x is increased by one. SPECIAL EXEPTION
    row = center
    col = center+1
    specialNumber = 2
    spiral[center][center + 1] = specialNumber
    spiralSideLength = 3

    #special case for the first spiral
    for i in range(spiralSideLength-2):
        row += 1
        specialNumber += 1
        spiral[row][col] = specialNumber
    for i in range(spiralSideLength-1):
        col -= 1
        specialNumber += 1
        spiral[row][col] = specialNumber
    for i in range(spiralSideLength-1):
        row -= 1
        specialNumber += 1
        spiral[row][col] = specialNumber
    for i in range(spiralSideLength-1):
        col += 1
        specialNumber += 1
        spiral[row][col] = specialNumber


    for circle in range(numOfSpirals-1):
        # checking if we hit the end
        if col + 1 > n - 1:
            return spiral
        col += 1
        specialNumber += 1
        spiral[row][col] = specialNumber
        spiralSideLength += 2

        #creating a spiral
        for i in range(spiralSideLength-2):
            row += 1
            specialNumber += 1
            spiral[row][col] = specialNumber
        for i in range(spiralSideLength-1):
            col -= 1
            specialNumber += 1
            spiral[row][col] = specialNumber
        for i in range(spiralSideLength-1):
            row -= 1
            specialNumber += 1
            spiral[row][col] = specialNumber
        for i in range(spiralSideLength-1):
            col += 1
            specialNumber += 1
            spiral[row][col] = specialNumber
    return spiral



# Input: handle to input file
#        the number spiral
# Output: printed adjacent sums
def print_adjacent_sums(in_data, spiral):
    #looping through the file IN CASE the first line is not a valid intiger
    data = in_data.readlines()
    summingList = []

    for line in data:
        try:
            # checking if even
            size = int(line)
            if int(line) % 2 == 0:
                size = int(line) + 1
            summingList.append(int(line))
        except:
            summingList.append(-1)

    # finding the first proper integer to start indixing
    startIndex = 0
    for num in range(len(summingList)):
        if summingList[num] != -1:
            startIndex = num
            break
    summingList = summingList[startIndex:]
    # Printing the sums
    for num in summingList:
        if num != -1:
            print(sum_adjacent_numbers(spiral, num))
        else:
            print("Invalid data")


# Input: spiral - the number spiral
#        n - the number to find the adjacent sum for
# Output: integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    sumReturn = 0

    # checking if the number exists in the spiral
    spiralEdge = len(spiral) - 1
    if n <= spiral[0][spiralEdge] and n >= 1:
        spiralCenter = int(len(spiral)/2)
        row = spiralCenter
        col = spiralCenter
        numberLocation = [0, 0]
        spiralSideLength = 1

        # finding the location of the number inside the spiral
        for highestNum in range(spiralCenter+1):
            if n < spiral[row][col]:
                # go clockwise to find the location of the number
                for i in range(spiralSideLength - 1):
                    row += 1
                    if spiral[row][col] == n:
                        numberLocation = [row, col]
                for i in range(spiralSideLength - 1):
                    col -= 1
                    if spiral[row][col] == n:
                        numberLocation = [row, col]
                for i in range(spiralSideLength - 1):
                    row -= 1
                    if spiral[row][col] == n:
                        numberLocation = [row, col]
                for i in range(spiralSideLength - 1):
                    col += 1
                    if spiral[row][col] == n:
                        numberLocation = [row, col]

            elif n == spiral[row][col]:
                numberLocation = [row, col]
            else:
                #checking for out of bound errors
                if row > 0:
                    row -= 1
                    col += 1
                    spiralSideLength += 2

        # a vector of direction to traverse all the surrounding nums [right, down, left, up, right, none] the reason
        # why I put right at the end and none one after is because one of the last operations is to calculate number
        # in the top right corner. Since the program knows what to grab from the directionVector because of
        # vectorLocation = [int(num/2), int(num/2+1)] it would run out of space by the last operation and grab the
        # empty vector and grabs the same cell as it would have done the second to last iteration.
        directionVector = [[0, 1], [1, 0], [0, -1], [-1, 0], [0, 1], [0, 0]]

        # summing all the numbers around the chosen one
        for num in range(8):
            try:
                # if the iterator is odd, we need to grab a diagonal direction (eg down & right)
                if num % 2 == 1:
                    vectorLocation = [int(num/2), int(num/2+1)]
                else:
                    vectorLocation = [int(num/2), 5]

                newLocationRow = numberLocation[0] + directionVector[vectorLocation[0]][0] + directionVector[vectorLocation[1]][0]
                newLocationCol = numberLocation[1] + directionVector[vectorLocation[0]][1] + directionVector[vectorLocation[1]][1]
                # checking if the new Location row & col are not out of bounds
                if newLocationRow >= 0 and newLocationRow <= spiralEdge and newLocationCol >= 0 and newLocationCol <= spiralEdge:
                    sumReturn += spiral[newLocationRow][newLocationCol]

            except:
                sumReturn += 0
        return sumReturn
    else:
        return 0






# Added for debugging only. No changes needed.
# Do not call this method in submitted version of your code.
def print_spiral(spiral):
    for i in range(0, len(spiral)):
        for j in range(0, len(spiral[0])):
            row_format = '{:>4}'
            print(row_format.format(spiral[i][j]), end='')
        print()
    print("___________________________________________________")


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # set the input source - change to False before submitting
    debug = True
    if debug:
        in_data = open('spiral.in')
    else:
        in_data = sys.stdin

    # process the lines of input
    size = get_dimension(in_data)

    # create the spiral
    spiral = [[]]
    spiral = create_spiral(size)
    # use following line for debugging only
    #print_spiral(spiral)

    # process adjacent sums
    print_adjacent_sums(in_data, spiral)


if __name__ == "__main__":
    main()
