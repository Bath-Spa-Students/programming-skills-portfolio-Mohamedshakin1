#Practice 2
"""Write an if-else statement that assigns O to the variable b if the variable a is less than 10.
Otherwise, it should assign 99 to the variable b."""

#Answer
a=int(input("Enter a number= "))
#if a is less than 10, it assigns value 0 to the variable b
#else, it assigns value 99 to the variable b
if a<10:
    b=0
else:
    b=99

print ("b=",b)