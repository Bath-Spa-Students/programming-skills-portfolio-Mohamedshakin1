#Practice 5
#Write a Python program to merge two dictionaries into one

#Answer

#First Dictionery
dict_1={'first_name1':'Mohamed',
        'last_name1':'Shakin',
        'age1':18}

#Second Dictionery
dict_2={'first_name2':'Abubakar',
        'last_name2':'Zahid',
        'age2':20}

#Two Dictionery merged into one
dict_1.update(dict_2)
print (dict_1)