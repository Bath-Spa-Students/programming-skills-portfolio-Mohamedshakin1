#Exercise 5
"""Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the
owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about
each pet"""

#Answer

#Creating each dictionary represents a different pet with the details of each pets
Kitten={"Species":"Cat",
        "Owner_name":"James"}
Puppy={"Species":"Dog",
       "Owner_name":"Bond"}
Goldfish={"Species":"Fish",
          "Owner_name":"Kaso"}
Parrot={"Species":"Bird",
        "Owner_name":"Aaron"}

#store all dictionery of each pets in list called pets
pets=[Kitten,Puppy,Goldfish,Parrot]
#print everything you know about each pet
for i in pets:
    print (i)