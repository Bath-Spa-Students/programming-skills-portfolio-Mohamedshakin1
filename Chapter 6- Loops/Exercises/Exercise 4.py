#Exercise 4
"""Make a list called sandwich_orders and fill it with the names of various sandwiches. 
Then make an empty list called finished_sandwiches.

Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. 
As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, 
print a message listing each sandwich that was made."""

#Answer
sandwich_orders=['Chicken', 'Vegetable', 'Egg', 'Cheese']
finished_sandwiches=[] #Empty list

#print a message for each order
for i in sandwich_orders:
    print ("I made your " + i + " sandwich")
    #Moving it to the list of finished sandwiches.
    finished_sandwiches.append(i)
    
#print a message listing each sandwich that was made.
for j in finished_sandwiches:
    print (j+ " is made")



