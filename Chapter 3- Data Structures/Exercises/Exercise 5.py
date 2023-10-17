#Exercise 5
"""You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.

•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

•Print a second set of invitation messages, one for each person who is still in your list."""

#Answer
names=["Azfar","Aseel","Suhail","Saif","Maahir","Tufail"]
#one of your guests can’t make the dinner
print (names[1],"can’t make the dinner")
#replacing the name of the guest who can’t make it with the name of the new person you are inviting.
names[1]="Umair"
#Print a second set of invitation messages, one for each person who is still in your list.
print (names[0]+", I am inviting you to dinner")
print (names[1]+", I am inviting you to dinner")
print (names[2]+", I am inviting you to dinner")
print (names[3]+", I am inviting you to dinner")
print (names[4]+", I am inviting you to dinner")
print (names[5]+", I am inviting you to dinner")
