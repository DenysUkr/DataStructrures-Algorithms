*#  File: Josephus.py
#  Student Name: Dennis Gao
#  Student UT EID: dg43333
#  Partner Name: Denys Osmak
#  Partner UT EID: do7369

import sys


# This class represents one soldier.
class Link(object):
    # Constructor
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class CircularList(object):
    # Constructor
    def __init__(self):
        self.first = None
        self.last = None

    # Is the list empty
    def is_empty(self):
        return self.first is None

    # Append an item at the end of the list
    def insert(self, data):
        item = Link(data)
        if self.data == None:
            self.data = item
        else:
            self.last.next = item
            item.next = self.first
            self.last = item

    # Find the node with the given data (value)
    # or return None if the data is not there
    def find(self, data):
        current = self.first
        while current != self.last:
            if current == data:
                return current
            current = current.next
        return None

    # Delete a Link with a given data (value) and return the node
    # or return None if the data is not there
    def delete(self, data):
        current = self.first
        if current.data == data and current.next != None:#if deleting the first element and there's more than one item in the list
            current = self.first.next
            self.last.next = self.first
            return current
        elif current.data == data and current.next == None:#if deleting and linked list has only 1 element
            current = None
            self.last = None
            return current
        while current != self.last:
            predecessor = current
            current = current.next
            if current == data:#if deleting in general
                predecessor.next = current.next
                return current
            elif current == data and current == self.last:#if deleting last element
                predecessor.next = current.next
                self.last = predecessor
                return current
        return None

    # Delete the nth node starting from the start node
    # Return the data of the deleted node AND return the
    # next node after the deleted node in that order
    def delete_after(self, start, step):
        current = start
        for i in range(step):
            predecessor = current
            current = current.next
        self.delete(current.data)
        return current, current.next

    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__(self):
        circleList = []
        current = self.first
        while current != self.last:
            circleList.append(current.data)
            current = current.next
        return circleList


# Input: Number of soldiers
# Outupt: Circular list with one link for each soldier
#         Data for first soldier is 1, etc.
def create_circular_list(num_soldiers):
    pass
    '''##### ADD CODE HERE #####'''


# Input: circular list representing soldiers
#        data for the soldier to start with (1, 2...)
#        number of soldiers to count before identifying one to die
# Output: printed list of soldiers, in order they died
def process_Josephus(my_list, num_soldiers, start_data, step_count):
    pass
    '''##### ADD CODE HERE #####'''


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Debug flag - set to False before submitting
    debug = True
    if debug:
        in_data = open('josephus.in')
        # in_data = open('autograde/test_cases/input_4.txt')
    else:
        in_data = sys.stdin

    # read the three numbers from the file
    line = in_data.readline().strip()
    num_soldiers = int(line)

    line = in_data.readline().strip()
    start_data = int(line)

    line = in_data.readline().strip()
    step_count = int(line)

    # Create cirular list
    my_list = create_circular_list(num_soldiers)

    # Kill off soldiers
    process_Josephus(my_list, num_soldiers, start_data, step_count)


if __name__ == "__main__":
    main()
