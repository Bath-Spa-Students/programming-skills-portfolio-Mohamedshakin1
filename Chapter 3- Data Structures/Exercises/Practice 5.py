#Practice 5
"""You have given a Python list. Write a program to find value 20 in the list, and if it is present,
replace it with 200. Only update the first occurrence of an item.
Work with the given list:
 list1 = [5, 10, 15, 20, 25, 50, 20]"""

#Answer
list1 = [5, 10, 15, 20, 25, 50, 20]
a=list1.index(20) #finds the index of first 20 in list1
list1[a]=200 #it updates the value 200 in place of first 20 
print (list1)