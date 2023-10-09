#Exercise 5
#She loves USB sticks and wants as many as she can get for £50.
cash=int(input("Enter the cash= "))
#They are £6 each
perpiece=6
pieces=cash//6
balance=cash%6
#how many USB sticks she can buy
print ("Total USB sticks purchased=",pieces)
#how many pounds she will have left.
print ("Balance pounds=",balance)