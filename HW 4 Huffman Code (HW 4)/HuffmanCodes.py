#  File: HuffmanCodes.py
#  Student Name: Denys Osmak
#  Student UT EID: do7369
# Python Huffman Compression
from PriorityQueue import PriorityQueue
import sys


# Huffman Node Class
class Huffman_Node(object):
    def __init__(self, ch=None, count=0, left=None, right=None):
        self.ch = ch
        self.count = count
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.count < other.count

    def __str__(self):
        if self.ch is None:
            ch = "*"
        else:
            ch = self.ch
        return ch + ", " + str(self.count)


# Build Character Frequency Table
# uses dictionary
# characters added in the order they first occur
def build_char_freq_table(inputString):
    # create output dictionary
    table = dict()

    for char in inputString:
        # checks if the char already exists in the table
        if char in table:
            table[char] += 1
        else:
            table[char] = 1
    return table


# Builds the Huffman Tree
# Creates Huffman Nodes, some pointing to others.
# Returns the root node
def build_huffman_tree(inputString):
    # Build the frequency table, a dictionary of character, frequency pairs
    freq_table = build_char_freq_table(inputString)

    # Build a priority queue, a queue of frequency, character pairs
    # Hightest priority is lowest frequency
    # When a tie in frequency, first item added will be removed first
    priorities = PriorityQueue()
    for key in freq_table:
        node = Huffman_Node(ch=key, count=freq_table[key])
        priorities.push(node)

    # Builds internal nodes of huffman tree, connects all nodes
    while (priorities.get_size() > 1):
        # creates pointers by poping the priorite queueue
        leftPt = priorities.pop()
        rightPt = priorities.pop()
        newNode = Huffman_Node(ch=None, left=leftPt, right=rightPt, count=(leftPt.count + rightPt.count) )
        priorities.push(newNode)  # reinserts the new combined node in the priority

    # At the end, priority queue is empty
    # Return the root node of the Huffman Tree
    return priorities.pop()


# After Huffman Tree is built, create dictionary of
# characters and code pairs
def get_huffman_codes(node, prefix, codes):
    if (node.left is None and node.right is None):
        codes[node.ch] = prefix
    else:
        get_huffman_codes(node.left, prefix + "0", codes)
        get_huffman_codes(node.right, prefix + "1", codes)
    return codes


# For each character in input file, returns the Huffman Code
# Input file uses <space> to indicate a space
# If character not found, display "No code found"
def process_chars(data, huff_codes):
    # printing header code
    print("Character    Code")

    # replacing all of the <space> inputs with " " to avoid errors
    for index in range(1, len(data)):
        if "space" in data[index]:
            data[index] = " "

    # skipped the first line of the input file
    for char in data[1:]:
        if char[0] in huff_codes:
            print(char[0], "          ", huff_codes[char[0]])
        else:
            print(char[0], "          ", "No code found")



''' DRIVER CODE '''

# Open input source
# Change debug to false before submitting
debug = False
if debug:
    in_data = open('message.in')
else:
    in_data = sys.stdin

# read message
data = in_data.readlines()
message = data[0].strip()

# Build Huffman Tree and Codes
root = build_huffman_tree(message)
huff_codes = get_huffman_codes(root, "", {})

# display code for each character in input file
process_chars(data, huff_codes)



