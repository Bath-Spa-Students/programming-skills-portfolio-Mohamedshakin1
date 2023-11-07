#Practice 5
"""Write a Python program that uses the elif statement to determine the season based on the
month provided as input."""

#Answer
month=input("Enter month= ")
#lower() is used to covert all letters of given words into small letters.
if month.lower() in ('december','january','february'):
    print ("It's Winter")

elif month.lower() in ('march','april','may'):
    print ("It's Spring")

elif month.lower() in ('june','july','august'):
    print ("It's Summer")

elif month.lower() in ('september','october','november'):
    print ("It's Autumn")