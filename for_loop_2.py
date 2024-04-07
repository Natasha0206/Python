#take email id as user input and print the username from the email address

email = input("Enter an email: ")
for i in email:
    if i == "@":
        break
    print(i,end="")
print()