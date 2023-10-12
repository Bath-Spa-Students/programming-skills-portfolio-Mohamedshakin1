#Exercise 5
"""A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. 
They are £6 each. Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
You will to use the arithmetic operators to complete this exercise."""

#Answer
#She loves USB sticks and wants as many as she can get for £50.
cash=50
print ("Cash entered=",cash)
#They are £6 each
perpiece=6
#how many USB sticks she can buy
pieces=cash//6
#how many pounds she will have left.
balance=cash%6
print ("Total USB sticks purchased=",pieces)
print ("Balance pounds=",balance)