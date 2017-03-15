#---------------------------------------------------------
# Morgan Jordan
# morgan.jordan@berkeley.edu
# Homework #3
# September 20, 2016
# README.txt
# README
#---------------------------------------------------------

(1)  For the file http://www.gutenberg.org/cache/epub/1342/pg1342.txt what is the depth of your tree?  What does that say about the number of operations to find a word?
The tree was 29 nodes deep, meaning 29 is also the maximum number of searches I would have to perform to find a word. 

(2)  What would happen if the input to your program were sorted (as it was in HW 1)?
If the text were already sorted, the creation of the BST would not take as long.

(3)  What are applications for binary search tree?  In what ways are they superior to lists?  In what ways are they inferior to lists?
Binary search trees can be used to search for something by separating all the values into parts and searching those separate parts. This makes searching and removing items faster too. This is all in contrast to linear lists, where the user may have to go through each item one by one to check values. On the flip side, items can be added to lists much fast, since they're just added to the end.     


(4)  Did you implement the extra credit (listed below)?  If so please explain your testing strategy on the extra credit.
No

(5) To test my code I insterted print statements throughout to ensure the information was flowing correctly. I forgot to return the recursive _find() functions, resulting a returned root.count with NoneType. At office hours, I realized this meant the root.count would never get updated, and added the return. I also had to figure out how to 