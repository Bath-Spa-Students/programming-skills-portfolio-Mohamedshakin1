#Exercise 4
"""Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message."""

#Answer
#Creating the fuction called make_shirt() that accepts a size and text of a message.

#size of the t-shirt is large by default and text of the t-shirt is I love Python by default.
def make_shirt(size="large", text="I love Python"):
    print ("t-shirt size number :",size)
    print ("text in t-shirt :",text)

#Calling the function

#size is large and text is I love Python by default if both argument is not entered
make_shirt() 

#first argument is entered but second argument is not entered, so it prints medium as size and 
#prints I love python as text by default
make_shirt("medium")

#it prints medium as size and Just Do It as text
make_shirt("medium","Just Do It")


