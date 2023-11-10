#Exercise 1
"""Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza."""

#Answer

while True:
    topping=input("Enter the topping you want to add: ")
    #if value is quit then loop ends, else loop will continue
    if topping.lower()=='quit':
        break
    print ("I will add "+topping+" in your pizza")
    

