#Practice 4
#Write a Python program that defines a function to calculate the area of a circle, and then calls that function with a given radius.

#Answer
#Creating the fuction called area()
def area(radius):
    #area of circle is 3.14 x r x r
    area=3.14*radius**2
    #prints area of circle.
    print (area, "cm square")

#Calling the function
area(5)
