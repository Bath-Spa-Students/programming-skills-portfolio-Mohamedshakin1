#Exercise 7
"""Think of at least five places in the world you’d like to visit.
•	 Store the locations in a list. Make sure the list is not in alphabetical order.

•	 Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.

•	 Use sorted() to print your list in alphabetical order without modifying the actual list.

•	 Show that your list is still in its original order by printing it.

•	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.

•	 Show that your list is still in its original order by printing it again.

•	 Use reverse() to change the order of your list. Print the list to show that its order has changed.

•	 Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.

•	 Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.

•	 Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed."""

#Answer
place=["West Bengal","Abu Dhabi","Zimbabwe","India","Bahrain"]
print (place)

#Use sorted() to print your list in alphabetical order without modifying the actual list.
alpha_order=sorted(place)
print ("List in alphabetical order without modifying the actual list:",alpha_order)

#Show that your list is still in its original order by printing it.
print ("List is still in its original order:",place)

#Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
alpha_order.reverse()
print ("List in reverse alphabetical order without modifying the actual list:",alpha_order)

#Show that your list is still in its original order by printing it again.
print ("List is still in its original order:",place)

#Use reverse() to change the order of your list. Print the list to show that its order has changed.
place.reverse()
print ("List is changed in reverse order:",place)

#Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
place.reverse()
print("List in its original order:",place)

#Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
place.sort()
print ("List is changed in alphabetical order:",place)

#Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
place.reverse()
print ("List is changed in reverse alphabetical order:",place)