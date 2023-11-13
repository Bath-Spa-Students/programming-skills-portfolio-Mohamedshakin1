#Exercise 2
"""Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call."""

#Answer
#Creating the fuction called favorite_book() that accepts one parameter, title.
def favorite_book(title):
    print ("One of my favourite book is",title) #print a message

#Taking input from user
title=input("Enter a book title :")

#Calling the function
favorite_book(title)