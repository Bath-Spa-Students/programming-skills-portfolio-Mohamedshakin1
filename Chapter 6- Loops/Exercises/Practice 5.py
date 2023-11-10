#Practice 5
"""Write a Python program that uses a while loop to find the largest number among a series of
user-input values until they enter '0' to exit the loop."""

#Answer
numbers=[]
#if number is equal to 0 then loop ends, else loop will continue adding numbers in list of numbers.
while True:
    n=int(input("enter a number= "))
    numbers.append(n)
    if n==0:
        break

print (numbers)
#max() is used to display largest number of series of numbers.
print ("largest number is",  max(numbers))
