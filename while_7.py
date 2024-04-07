#using while loop take numbers as input from user 
#and keep adding them until user presses 0,
#then display the total sum

Total = 0 
while True:
    inp = int(input("Enter the number:"))
    Total += inp
    if inp == 0:
        break
print(Total)


# using while loop take alphanumeric characters as input from user and keep adding them until user presses ' . ' then display the final string

final = ""
while True:
    string = input("Enter the string:")
    final += string
    if string == ".":
        break
print(final)
    