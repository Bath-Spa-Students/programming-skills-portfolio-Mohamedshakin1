#Exercise 6
"""You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.

•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, 
print a message to that person letting them know you’re sorry you can’t invite them to dinner.

•Print a message to each of the two people still on your list, letting them know they’re still invited.

•Use del to remove the last two names from your list, so you have an empty list. 
Print your list to make sure you actually have an empty list at the end of your program."""

#Answer
"""Use pop() to remove guests from your list one at a time until only two names remain in your list. 
Each time you pop a name from your list, 
print a message to that person letting them know you’re sorry you can’t invite them to dinner."""
names=["Azfar","Aseel","Suhail","Saif","Maahir","Tufail"]
not_invited=names.pop()
print(not_invited+", I am sorry I can’t invite you to dinner.")
not_invited=names.pop()
print(not_invited+", I am sorry I can’t invite you to dinner.")
not_invited=names.pop()
print(not_invited+", I am sorry I can’t invite you to dinner.")
not_invited=names.pop()
print(not_invited+", I am sorry I can’t invite you to dinner.")

#Print a message to each of the two people still on your list, letting them know they’re still invited.
print(names[0]+", you are still invited")
print(names[1]+", you are still invited")

"""Use del to remove the last two names from your list, so you have an empty list. 
Print your list to make sure you actually have an empty list at the end of your program."""
del names[0]
del names[0]

print(names)

