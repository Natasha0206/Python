#print every letter and index number of the 
#string taken as input from user in format "{letter}, {index}"

string = input("Enter your string:")

for i in range(0,len(string)):
    print(string[i],i)