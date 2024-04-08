#  File: BST_Cipher.py
#  Student Name: Medhavi Jambhekar
#  Student UT EID: mj32463
#  Partner Name: Denys Osmak
#  Partner UT EID: do7369
import sys

# One node in the BST Cipher Tree
class Node:
    def __init__(self, ch):
        self.ch = ch
        self.left = None
        self.right = None


# The BST Cipher Tree
class Tree:

    # Create the BST Cipher tree based on the key
    def __init__(self, key):
        # This is for debug purposes only.
        # Comment out or delete before submitting.
        # key_tree.BST_print()
        # removes invalid characters and makes everything lowercase
        key = self.clean(key.lower())
        # set root to first character in the input string
        self.root = Node(key[0])

        # iterate over remaining characters
        for a in range(1, len(key)):
            current = self.root

            while current:
                # char is less than key[a]-- key[a] comes before current
                if current.ch < key[a]:
                    # creates right child if the right child doesn't exist
                    if current.right is None:
                        current.right = Node(key[a])
                        break # we found a spot for this character, we can move on to the next char in the string
                    # if right child exists, move current to right child
                    current = current.right

                # char is greater than key[a] -- key[a] comes after current in alphabet
                elif current.ch > key[a]:
                    # creates left child if there isn't an existing left child
                    if current.left is None:
                        current.left = Node(key[a])
                        break
                    current = current.left

                else:
                    break # breaks if the current character is equal to key[a], we don't want repeat letters in the
                    # tree


    # Insert one new charater/Node to the BST Cipher tree
    # If the character already exists, don't add it.
    def insert(self, ch):
        current = self.root

        # checking if the character is a letter and not a random character
        if self.isValidCh(ch):
            while current:
                if current.ch < ch:
                    # add node to right child if there's no node already existing there
                    if current.right is None:
                        current.right = Node(ch)
                        break
                    current = current.right

                elif current.ch > ch:
                    # add node to right child if there's no node already existing there
                    if current.left is None:
                        current.left = Node(ch)
                        break
                    current = current.left

                else:
                    break

    # Encrypts a text message using the BST Tree
    def encrypt(self, message):
        encryptedString = ""
        for character in message:
            #checking if the character is a valid character
            if self.isValidCh(character):
                encryptedString = encryptedString + self.encrypt_ch(character)

        #remove the last "!" from the string
        encryptedString = encryptedString[:-1]
        return encryptedString

    # Encrypts a single character
    def encrypt_ch(self, ch):
        outString = ""
        current = self.root

        # if the key is in the root
        if self.root.ch == ch:
            return "*!"

        # looping through the entire tree
        while current != None:
            # if the key is found
            if current.ch == ch:
                break
            # if the key is less than current data then move to the left child
            elif current.ch > ch:
                current = current.left
                outString = outString + "<"
            # if the key is greater than current data then move to the right child
            elif current.ch < ch:
                current = current.right
                outString = outString + ">"
        # add ! to end of each letter and return encrypted letter
        return outString + "!"



    # Decrypts an encrypted message using the BST Tree
    def decrypt(self, codes_string):
        # adding a "!" to encoded message since its used as a logic statement in the loop
        codes_string = codes_string + "!"
        decryptionSting = ""
        codedSnipped = ""

        # grab the entire string snipped between ! and another !
        for character in codes_string:
            codedSnipped = codedSnipped + character

            # if found the end of coded snipped run the decryption code
            if character == "!":
                decryptionSting = decryptionSting + self.decrypt_code(codedSnipped)
                # reseting the coded string
                codedSnipped = ""

        return decryptionSting

    # Decrypts a single code
    def decrypt_code(self, code):
        current = self.root

        # if the key is in the root
        if code == "*":
            return self.root.ch

        # looping through the entire code
        for char in code:
            # if the key is found
            if char == "!":
                return current.ch
            # if the code points to left then move to the left child
            elif char == "<":
                # if encoded message is going out of bounds of BST then return ""
                try:
                    current = current.left
                except:
                    return ""
            # if the code points to right then move to the right child
            elif char == ">":
                # if encoded message is going out of bounds of BST then return ""
                try:
                    current = current.right
                except:
                    return ""
        return

    # Get printed version of BST for debugging
    def BST_print(self):
        if self.root is None:
            return "Empty tree"
        self.BST_print_helper(self.root)

    # Prints a BST subtree
    def BST_print_helper(self, node, level=0):
        if node is not None:
            if node.right is not None:
                self.BST_print_helper(node.right, level + 1)
            print('     ' * level + '->', node.ch)
            if node.left is not None:
                self.BST_print_helper(node.left, level + 1)

    def clean(self, text):
        cleanText = ""
        for i in range(len(text)):
            if (self.isValidCh(text[i])):
                cleanText += text[i]
        return cleanText

    # Utility method
    def isValidLetter(self, ch):
        if (ch >= "a" and ch <= "z"):
            return True
        return False

    # Utility method
    def isValidCh(self, ch):
        if (ch == " " or self.isValidLetter(ch)):
            return True
        return False


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('bst_cipher.in')
    else:
        in_data = sys.stdin

    # read encryption key
    key = in_data.readline().strip()

    # create a Tree object
    key_tree = Tree(key)

    # read string to be encrypted
    text_message = in_data.readline().strip()

    # print the encryption
    print(key_tree.encrypt(text_message))

    # read the string to be decrypted
    coded_message = in_data.readline().strip()

    # print the decryption
    print(key_tree.decrypt(coded_message))


if __name__ == "__main__":
    main()