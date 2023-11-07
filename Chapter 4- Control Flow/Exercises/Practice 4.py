#Practice 4
"""Write a python program with an if-else statement that displays Speed is normal if the speed
variable is within the range of 24 to 56. If the speed variable's value is outside this range, display 'Speed is abnormal"""

#Answer
speed=int(input("Enter the speed= "))
if speed in range(24,57):
    print ("Speed is normal")

elif speed not in range(24,57):
    print ("Speed is abnormal")


