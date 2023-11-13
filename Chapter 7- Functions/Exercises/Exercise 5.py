#Exercise 5
"""Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, 
such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities,
at least one of which is not in the default country."""

#Answer
#Calling the function

#Creating the fuction called describe_city() that accepts the name of a city and its country.
#Parameter for the country is UAE by default.
def describe_city(city,country="UAE"):
    print (city, "is in", country)

#Calling the function

#first argument is entered but second argument is not entered, so it prints Dubai as city and 
#prints UAE as country by default
describe_city("Dubai")

#first argument is entered but second argument is not entered, so it prints Sharjah as city and 
#prints UAE as country by default
describe_city("Sharjah")

#first and second argument is entered, so it prints Mumbai as City and Just Do It as Country.
describe_city("Mumbai","India")