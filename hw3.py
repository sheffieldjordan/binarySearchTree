#---------------------------------------------------------
# Morgan Jordan
# morgan.jordan@berkeley.edu    
# Homework #3
# September 20, 2016
# hw3.py
# Main
#---------------------------------------------------------

from BST import *

def read_file(filename):
    with open(filename, 'rU') as document:
        text = document.read()
    filter_punc = lambda t: ''.join([x.lower() for x in t if x.isalpha()])
    words = [x for x in map(filter_punc, text.split()) if x]
    return words


def main():
    while(True):
        print("Enter the file name to read:")
        filename = input('> ')
        try:
            words = read_file(filename)
        except IOError:
            print("Unable to find the file {}".format(filename))
        else:
            tree = BSTree()
            for word in words:
                tree.add(word)
            break

    ######################
    # Begin Student Code #
    ######################
    #Functions for use
    while(True):
        try:
            query = ""
            query = input("Query?  ")
            if query == "terminate":
                break
            if query == "stats":
                print("Tree size: ", tree.size())
                print("Tree height: ", tree.height())
            else:
                print("The word {} appears {} times in the tree.".format(query, tree.find(query)))
        except AttributeError: #to account for words entered that are not in the tree. Otherwise, it would throw an attribute error
            print("The word {} appears 0 times in the tree.".format(query))
    # print(tree.find("the"))        
    # tree.inOrderPrint()


if __name__ == "__main__":
    main()