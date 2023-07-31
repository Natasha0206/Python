#Python If-Else
#Task
#Given an integer, , perform the following conditional actions:

#If  is odd, print Weird
#If  is even and in the inclusive range of  to , print Not Weird
#If  is even and in the inclusive range of  to , print Weird
#If  is even and greater than , print Not Weird


n=int(input())
if (n%2!=0):
    print("Weird")
elif (n%2==0 and 1<n<6):
    print("Not Weird")
elif (n%2==0 and 5<n<21):
    print("Weird")
else:
    print("Not Weird")
