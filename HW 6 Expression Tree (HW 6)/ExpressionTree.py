#  File: ExpressionTree.py
#  Student Name: Xinlin Cao
#  Student UT EID: xc5374
#  Partner Name: Denys Osmak
#  Partner UT EID: DO7369

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
class Stack(object):
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
class Tree(object):
    def __init__(self):
        self.root = Node(None)

    # Input: a string expression
    # Output: an expression tree
    def create_tree(self, expr):
        # create a stack for numbers and operands
        nodeStack = Stack()
        current = self.root

        characters = expr.split()
        # characters = characters[1:] # starting from the seccond line to make up for an already empy node at root

        # looping through the string expression
        for char in characters:
            if char == "(":
                newNode = Node(None)
                current.lChild = newNode
                nodeStack.push(current)
                current = current.lChild
            elif char.isdigit() or "." in char:
                current.data = char
                current = nodeStack.pop()
            elif char in operators:
                current.data = char
                newNode = Node(None)
                current.rChild = newNode
                nodeStack.push(current)
                current = current.rChild
            elif char == ")":
                if not nodeStack.is_empty():
                    current = nodeStack.pop()
        # returning root
        return current


    # Input: A node in an expression tree
    # Output: The result of evaluating the expression
    #         with this node as the root
    def evaluate(self, current):
        # if current is an integer aka a leaf node
        if current.data not in operators:
            return current.data
        # traverse the left child
        leftEquation = self.evaluate(current.lChild)

        # traverse the right child
        rightEquation = self.evaluate(current.rChild)

        # use operation to evaluate the node
        return float(operation(current.data, leftEquation, rightEquation))


    # Starter Method for pre_order
    # Input: a node in an expression tree
    # Output: (string) the preorder notation of the expression
    #                  with this node a the root
    def pre_order(self, current):
        # empty string to store data
        order = ""
        # if current is an operator, add data to string;
        if current.data in operators:
            order += current.data + " "

            # check if left child is a number, add data to string;
            # recursively add current to string if not
            if current.lChild.data.isdigit():
                order += current.lChild.data + " "
            else:
                order += self.pre_order(current.lChild)

            # check if right child is a number, add data to string;
            # recursively add current to string if not
            if current.rChild.data.isdigit():
                order += current.rChild.data + " "
            else:
                order += self.pre_order(current.rChild)

        # current data is a number, directly add to string
        else:
            order += current.data + " "

        return order



    # Starter Method for post_order
    # Input: a node in an expression tree
    # Output: (string) the post order notation of the expression
    #                  with this node a the root
    def post_order(self, current):
        # if current is an operator, recursively traverse left child
        if current.data in operators:
            lexpr = self.post_order(current.lChild)

        # return if current data is not an operator (is a number)
        if current.data not in operators:
            return current.data
        # if current is an operator, recursively traverse right child;
        # return combined string expression
        else:
            rexpr = self.post_order(current.rChild)
            return lexpr + " " + rexpr + " " + current.data


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():
    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('expression.in')
    else:
        in_data = sys.stdin

    # read infix expression
    line = in_data.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())


if __name__ == "__main__":
    main()
