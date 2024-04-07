#using for loop, reverse a string

string=input("Enter the string:")
for i in range(-1,-len(string)-1,-1):
    print(string[i])

#Without using for loop, reverse a string

string=input("Enter the string:")
print(string[-1:-len(string)-1:-1])