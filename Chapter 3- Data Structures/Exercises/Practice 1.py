#Practice 1
"""Given a Python list, write a program to remove all occurrences of item 20.
Given list:
list1 = [5, 20, 15, 20, 25, 50, 20]"""

#Answer
list1=[5,20,15,20,25,50,20]

#it removes all occurrences of item 20 in list1
for i in list1:
    if 20 in list1:
        list1.remove(20)

print (list1)