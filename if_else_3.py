# take user's age and gender as inputs and then check if user is male
# or female and if user is male check if he is above or below 18. 
# Same for female. If yes print "Below/Above Male/Female".

age = int(input("Enter age:"))
gender = input("Enter sex:")

if gender == "Male" or gender == "M" or gender == "male" or gender == "m" :
    print("user is Male")
    if age < 18:
        print("Male is below 18")
    else:
        print("Male is equal to 18 or above 18")
    
elif gender == "Female" or gender == "F" or gender == "Female" or gender == "f":
    print("user is  Female")
    if age < 18:
        print("Female is below 18")
    else:
        print("Female is equal to 18 or above 18")
else:
    print("Not considered")