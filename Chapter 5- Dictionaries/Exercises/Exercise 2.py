#Exercise 2
"""A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

* Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store 

their meanings as values.

* Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print 

the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between 

each word-meaning pair in your output."""

#Answer
glossary={'print':'is to display output',
          'comment':'is to note down the explaination',
          'variable':'name that represents a value stored',
          'string':'sequence of character that is enclosed with quotation mark',
          'type':'it returns the type of given variable'}

for key, value in glossary.items():
    print ('\n',key,":",value)


