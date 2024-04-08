import sys

# list of valid operators
operators = ['+', '-', '*', '/', '//', '%', '**']


# Input: Elements of a simple expression
#        operator (String) and two operands (numbers)
# Output: result of evaluation of the expression
def operation(operator, n, m):
    expression = str(n) + operator + str(m)
    return eval(expression)


# Stack Class - DO NOT CHANGE
# Traditional Stack implementation containing list of data items
# Used to keep track of items in nested expressions.
class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if (not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0


# Node Class
# Purpose: Used by the Tree Class to represent one operand or operators
#          in a binary expression. It includes data (a character) and
#          two pointers, to the left and right child nodes.
# You do not need to make changes to this class.
class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild


# Tree Class
# Purpose: To represent the string representation of operators and operands
#          of a binary expression so it can be evaluated.
# You need to make a lot f changes to this class!
class Tree (object):
    def __init__(self):
        self.root = Node(None)

    # Input: a string expression
    # Output: an expression tree
    def create_tree(self, expr):
        # creating a tree object
        tree = Tree()

        # create a stack for numbers and operands
        operandStack = Stack()
        numberStack = Stack()

        # looping through the string expression
        for char in expr:
            if char.isdigit():
                numberStack.push(char)
            elif char in operators:
                operandStack.push(char)
            if char == ")":
                # if empty tree
                if tree.root == None:
                    leftNode = Node(numberStack.pop)
                    rightNode = Node(numberStack.pop)
                    newNode = Node(data=operandStack.pop, lChild=leftNode, rChild=rightNode)
                    tree.root = newNode
                #if not empty tree
                else:
                    rightNode = Node(numberStack.pop)
                    newNode = Node(data=operandStack.pop, lChild=tree.root, rChild=rightNode)
                    tree.root = newNode
        return tree


