import sys

# a queue class, tested and working


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)

    # checks the item at the top of the Queue
    def peek(self):
        return self.queue[0]

    # check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # return the size of the queue
    def size(self):
        return len(self.queue)


# Node class that defines items in the Tree
class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# The Binary Search Tree class
class BST(object):
    def __init__(self, int_list=None):
        self.root = None
        if int_list is not None:
            for num in int_list:
                self.insert(num)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_helper(self.root, data)

    def insert_helper(self, node, data):
        # Compare the new value with the parent node
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert_helper(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert_helper(node.right, data)

    def getSpaces(self, num):
        spaces = ""
        for i in range(num):
            spaces += "    "
        return spaces

    # Print the tree
    def printTree(self):
        if (self.root is None):
            return
        else:
            self.printTreeHelper(self.root)

    def printTreeHelper(self, node, level=0):
        if node.right:
            self.printTreeHelper(node.right, level+1)
        print(self.getSpaces(level), node.data, "-----")
        if node.left:
            self.printTreeHelper(node.left, level+1)


    def is_complete(self):
        pass
        #add root node to queue

        # while queue not empty
            # if item is top of array is None and queue is not empty return false
            # add left child of node on top of queue
            # add rigth child of node on top of queue
            #pop Queuq

    # Returns True if two BSTs are similar
    def is_similar(self, compTree):
        # storing the values of in oderd traveral of the two trees
        curentTree = []
        self.similarHelper(self.root, curentTree)
        competitorTree = []
        compTree.similarHelper(compTree.root, competitorTree)

        #print(curentTree, " <--- CUR vs COMP ---> ", competitorTree)

        # compering if trees return the same numbers
        if curentTree == competitorTree:
            return True
        return False


    def similarHelper(self, node, out):
        # in order traversal of the tree
        if node is None:
            return

        self.similarHelper(node.left, out)
        #print(node.data)

        out.append(str(node.data)) # returning the value of node to compare it
        self.similarHelper(node.right, out)





"""    # Returns True if two BSTs are similar
    def is_similar(self, compTree):
        # traverse an entrie tree
        return self.similarHelper(self.root, compTree.root)

            # check if each node's data, left, and right are the same between self and compTree (return false if not the same)


        # return true in the end


    def similarHelper(self, node, compNode):

        if node is None or compNode is None:
            return

        # see if node.data matches
        if node.data != compNode.data:
            return False

        # see if left children mathc
        self.similarHelper(node.left, compNode.left)

        # see if right children mathc
        self.similarHelper(node.right, compNode.right)

        return True"""








''' DRIVER CODE '''
# Don't change code below, except for the debug flag.

# Debug flag - set to False before submitting
debug = True
if debug:
    in_data = open('bst_util.in')
else:
    in_data = sys.stdin

# read number of trees
numTrees = int(in_data.readline())
trees = []

# build list of trees
for i in range(numTrees):
    line = in_data.readline()
    line = line.strip()
    line = line.split()
    tree_input = list(map(int, line)) 	# converts elements into ints
    trees.append(BST(tree_input))
    if debug:
        trees[i].printTree()

# run utility methods
num_similar = 0
num_complete = 0
for i in range(numTrees):
    for j in range(i + 1, numTrees):
        if (i != j and trees[i].is_similar(trees[j])):
            num_similar += 1
    if (trees[i].is_complete()):
        num_complete += 1

print(num_similar)
print(num_complete)
