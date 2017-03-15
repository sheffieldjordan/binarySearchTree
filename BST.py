#---------------------------------------------------------
# Morgan Jordan
# morgan.jordan@berkeley.edu
# Homework #3
# September 20, 2016
# BST.py
# BST
# ---------------------------------------------------------

class Node:
    #Constructor Node() creates node
    def __init__(self,word):
        self.word = word #to create an instance object of a Node class, 
        #you need to tell the Node what word it is. Word will then be associated
        # with the particular instance you create.  
        self.right = None 
        self.left = None
        self.count = 1

class BSTree:
    #Constructor BSTree() creates empty tree
    def __init__(self, root=None):
        self.root = root # to create an instance object of the BSTree class,
        # you need to tell the tree what it's root is. The default root is empty. 
    
    #These are "external functions" that will be called by your main program - I have given these to you
    
    #Find word in tree
    def find(self, word):
        return _find(self.root, word)
        # a =  _find(self.root, word)
        # print('in find() a = ', a)
        # return a
    
    #Add node to tree with word
    def add(self, word):
        if not self.root:
            self.root = Node(word)
            return
        _add(self.root, word)

    #Print in order entire tree
    def in_order_print(self):
        _in_order_print(self.root)

    def size(self):
        return _size(self.root)

    def height(self):
        return _height(self.root)


#These are "internal functions" in the BSTree class - You need to create these!!!

#Function to add node with word as word attribute
def _add(root, word):
    if root.word == word: #if 50 == 38
        root.count +=1
        return #root.count
    if root.word > word:
        if root.left == None:  
            root.left = Node(word) 
        else:
            _add(root.left, word)
    else:
        if root.right == None:
            root.right = Node(word) #instatiating a new Node class >> a new node that contains whatever the word 
        else:
            _add(root.right, word)
    
#Function to find word in tree
def _find(root, word):
    """this performs a binary search to see if the word is in
    the tree, if so, returns the number of times the word appears
    in the input text file; find(word) is fully recursive """
    if root.word == word:
        # print('found the word, count is', root.count)
        return root.count
    if root.word > word:
        return _find(root.left, word)
    if root.word < word:
        return _find(root.right, word)
   

#Get number of nodes in tree
def _size(root):
    if root is None:
        return 0
    if root is not None:
        return 1 + _size(root.left) + _size(root.right)

#Get height of tree
def _height(root):
    if root is None:
        return 0 ; 
    else:
        left_height = _height(root.left)
        right_height = _height(root.right)
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1
#Function to print tree in order
def _in_order_print(root):
    if not root: #if root == None # if root is None
        return #closes out of the very last function call and continues with the next to last one, skips to root.word
    _in_order_print(root.left)
    print(root.word)
    print(root.count) #assume this is 1
    _in_order_print(root.right)
