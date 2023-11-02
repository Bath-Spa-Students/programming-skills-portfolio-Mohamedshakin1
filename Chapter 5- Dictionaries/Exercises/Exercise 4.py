#Exercise 4
"""Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

* Use a loop to print the name of each river included in the dictionary.

* Use a loop to print the name of each country included in the dictionary."""

#Answer
river={'Godavari':'India','Koshi':'Nepal','Kundar':'Pakistan'}

#Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
for key,value in river.items():
    print ("The",key,"runs through",value)

#Use a loop to print the name of each river included in the dictionary.
for key,value in river.items():
    print (key)

#Use a loop to print the name of each country included in the dictionary.
for key,value in river.items():
    print (value)