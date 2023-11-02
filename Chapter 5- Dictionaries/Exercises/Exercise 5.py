#Exercise 5
"""Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the
owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about
each pet"""

#Answer
Kitten={"Species":"Cat",
        "Owner_name":"James"}
Puppy={"Species":"Dog",
       "Owner_name":"Bond"}
Goldfish={"Species":"Fish",
          "Owner_name":"Kaso"}
Parrot={"Species":"Bird",
        "Owner_name":"Aaron"}

pets=[Kitten,Puppy,Goldfish,Parrot]
for i in pets:
    print (i)