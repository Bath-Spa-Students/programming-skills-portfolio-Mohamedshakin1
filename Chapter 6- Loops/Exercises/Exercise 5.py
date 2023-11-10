#Exercise 5
"""Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. 
Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to 
remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches."""

#Answer
print ("the deli has run out of pastrami")
sandwich_orders=['Chicken', 'Vegetable', 'Egg', 'Cheese', 'pastrami','pastrami','pastrami']
finished_sandwiches=[]

#Loop will continue running as long as pastrami is there in the list of sandwich orders, else loop ends.
while True:
    if 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')

    else:
        break

#Moving it to the list of finished sandwiches.
for i in sandwich_orders:
    finished_sandwiches.append(i)

#print a message listing each sandwich that was made.
for j in finished_sandwiches:
    print (j+ " is made")