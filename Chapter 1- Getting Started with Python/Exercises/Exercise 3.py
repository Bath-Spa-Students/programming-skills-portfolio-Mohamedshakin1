#Exercise 3
"""Write a Python program to display the current date and time."""

#Answer
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))