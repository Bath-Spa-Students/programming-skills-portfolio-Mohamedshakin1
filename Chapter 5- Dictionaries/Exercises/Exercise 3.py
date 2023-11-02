#Exercise 3
"""Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 

to your glossary.When you run your program again, these new words and meanings should automatically be included in the output."""

#Answer
glossary={'print':'is to display output',
          'comment':'is to note down the explaination',
          'variable':'name that represents a value stored',
          'string':'sequence of character that is enclosed with quotation mark',
          'type':'it returns the type of given variable'}

for key, value in glossary.items():
    print ("\n",key,value)

#add five more Python terms to your glossary
glossary["dictionary"]="A collection of key-value pairs"
glossary["int"]="numerical value without decimal point"
glossary["float"]="numerical value with decimal point"
glossary["Boolean"]="An expression that evaluates to True or False"
glossary["List"]="Collection of items enclosed with square bracket"

print (glossary)