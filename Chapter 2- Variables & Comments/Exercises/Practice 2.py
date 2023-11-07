#Practice 2
"""Write a python program that takes courses marks as input and then calculates average of all the
courses. After calculating the average, calculate the percentage of a student using total marks. Assume
the total of all the courses marks is 500 or take the total marks from the user as input."""

#Answer
course1= int(input("Enter the mark of course 1= "))
course2= int(input("Enter the mark of course 2= "))
course3= int(input("Enter the mark of course 3= "))
course4= int(input("Enter the mark of course 4= "))
course5= int(input("Enter the mark of course 5= "))
sum= course1+course2+course3+course4+course5

#calculates average of all the courses
average=sum/5

#calculate the percentage of a student using total marks
percentage=(sum/500) *100

print ("Average of all courses=",average)
print ("the percentage of a student=",percentage)
