#Practice 4
#Write a Python program that uses the break statement to exit a for loop when a specific condition is met.

#Answer
list1=[]
while True:
    name=input("Enter a name: ")
    # if name is equal to exit then loop ends, else loop will continue adding names in list.
    if name.lower()=="exit":
        break
    else:
        list1.append(name)
print (list1)

