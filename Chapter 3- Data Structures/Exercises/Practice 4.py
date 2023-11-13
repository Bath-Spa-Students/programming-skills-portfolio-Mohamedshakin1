#Practice 4
"""Assume the lists numbers1 has 100 elements and numbers2 is an empty list. Write code that
copies the values in numbers1 to numbers2."""

#Answer

#list numbers1 has 100 elements
numbers1=[]
for i in range (1,101):
    numbers1.append(i)

#list numbers2 is an empty list
numbers2=[]
print ("before copying to numbers2:",numbers2)
#copying the values in numbers1 to numbers2.
numbers2=numbers1
print ("after copying to numbers2:",numbers2)