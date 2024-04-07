# check if person's age is above 18, equal to 18 or below 18,
# if above print "above" if below print "below" if equal print "equal

age = int(input("Enter age:"))
if age < 18:
    print("Below")
elif age > 18:
    print("Above")
else:
    print("Equal")