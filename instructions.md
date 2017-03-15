WORD Count Program

1) ask the user for a local file to read (use this to test >> http://www.gutenberg.org/cache/epub/1342/pg1342.txt)
2) remove all non-alphabetic characters (including punctuation and digits)
3) change any capitalized character into lower-case format (a word is defined as a sequence of characters separated by white spaces and new lines)
Thus, "Darcy's" becomes the word "darcys".
 
4) Define a new class BST that implements a binary search tree.
5) implement the following methods 
•__init__
•size (giving the number of entries in the tree) 
•height (giving the depth of the tree)
•find(word) - this performs a binary search to see if the word is in the tree, if so, returns the number of times the word appears in the input text file; find(word) and add(word) should be fully recursive functions
•add(word) -- if the word is not already in the tree, this adds it with an initial count of one.  If the word is present, this increments it by one; find(word) and add(word) should be fully recursive functions
 
Each node in the tree may keep track of the depth of the current subtree and the number of entries below it

A) After the work is loaded into the dictionary, the program should run a main loop that takes as input a test word, and finds if it is in the BST.  The format should look exactly like this
 
Query?  elizabeth
The word elizabeth appears XXX times in the tree 
 
B) If the key word "stats" is given, the program should print out the number of entries in the tree and the maximum depth of the tree.

C) If the key word "terminate" is given, the program should terminate.

6) >>> Answer the following questions and include the answers in a README file:
 
(1)  For the file http://www.gutenberg.org/cache/epub/1342/pg1342.txt what is the depth of your tree?  What does that say about the number of operations to find a word?
(2)  What would happen if the input to your program were sorted (as it was in HW 1)?
(3)  What are applications for binary search tree?  In what ways are they superior to lists?  In what ways are they inferior to lists?
(4)  Did you implement the extra credit (listed below)?  If so please explain your testing strategy on the extra credit.
 
Extra credit:  For extra credit, modify "add(word)" so that as it adds words to the tree, it keeps the tree balanced through tree rotation, so that every leaf node differs by at most one in depth.  See http://en.wikipedia.org/wiki/Tree_rotation for details.

Please extensively test your assignment.  We will cover testing scripts in lab section.  
 
*5) In your README file, also explain how you tested your program (what test cases and strategies did you use) and don't forget the answers to the questions above.  You will turn in the following files.
 
hw3.<USERID>.py
hw3.<USERID>.BST.py
hw3.<lUSERID>.test.py
hw3.<USERID>.README.txt
 
Upload these files using the file upload tool available at:: https://www.ischool.berkeley.edu/uploader/?s=i206 .  Login with your ISchool userid and password and follow the directions.


Click here to view. Search or link to this question with @38. 
