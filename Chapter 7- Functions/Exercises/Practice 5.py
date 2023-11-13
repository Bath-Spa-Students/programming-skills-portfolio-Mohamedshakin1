#Practice 5
#Write a Python program that defines a function to check whether a given number is prime.

#Answer
#Prime numbers are natural numbers that are divisible by only 1 and the number itself.
#For example 3 is a prime number because 3 are divisible by only two number that are 1 and 3, not by other numbers.

#Creating the fuction called prime()
def prime(num):
    #Creating empty list
    list1=[]
    #starting number is 1 and ending number is variable num.
    for i in range(1,num):
        #it checks if the given number is divisible by any of the numbers
        if num%i==0:
            list1.append(i) #The given number that is divisible by any of the numbers that numbers will be added to the list.

#if there are more than two numbers in list, its not a prime number.
#if there is 1 or 2 numbers in list, its a prime number.
    if len(list1)>1:
        print (num, "is not a prime number")
    else:
        print (num, "is a prime number")

prime (23)
prime(6)


