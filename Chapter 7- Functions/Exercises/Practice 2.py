#Practice 2
#Write a Python function that calculates the factorial of a given positive integer using recursion.

#Answer

#Creating the fuction called factorial() 
def factorial(num):
    #Factorial of 0 and 1 is 1
    if num==0 or num==1:
        return 1
    #Factional of n is n*(n-1)*(n-2)*.....*1
    else:
        return num*factorial(num-1)

#Calling the function    
print (factorial(5))