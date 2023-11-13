#Exercise 3
"""Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function 
should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional 
arguments to make a shirt. Call the function a second time using keyword arguments."""

#Answer
#Creating the fuction called make_shirt() that accepts a size and text of a message.
def make_shirt(size,text):
    print ("t-shirt size :",size) #prints size of the t-shirt
    print ("text in t-shirt :",text) #prints texts of the t-shirt

#Calling the function

#Positional arguments
make_shirt("large","Not Out") #size is large and text is Not Out

#Keyword arguments
make_shirt(text="Never Ever", size="small") #size is small and text is Never Ever