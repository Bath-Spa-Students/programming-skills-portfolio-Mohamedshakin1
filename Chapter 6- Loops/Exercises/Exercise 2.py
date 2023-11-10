#Exercise 2
"""A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; 
if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. 
Write a loop in which you ask users their age, and then tell them the cost of their movie ticket."""

#Answer

#if value is -1 then loop ends, else loop will continue
print ("type -1 to quit")
while True:
    age=int(input("Enter the person's age: "))
    cost=0
    if age<3 and age>-1:
        cost+=0
        print ("Your total ticket cost is free")
    elif age>=3 and age<=12:
        cost+=10
        print ("Your total ticket cost is",cost)
    elif age>12:
        cost+=15
        print ("Your total ticket cost is",cost)
    else:
        print ("Thank you for visiting")
        break
    
