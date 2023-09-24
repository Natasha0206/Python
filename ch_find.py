ch = input("Enter a single digit:")
if ch >='A' and ch <='Z':
    print("You have entered a Capital letter.")
elif ch >='a' and ch <='z':
    print("You have entered a Small letter.")
elif ch >='0' and ch <='9':
    print("You have entered a Special Character.")
else:
    print("Yov have entered Special characters.")