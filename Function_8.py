# write a function to print user inputted string,
# if no input given print 'hello' by default

string = input("Enter string:")
def user():
    if string == "":
        print("Hello")
    else:
        print(string)
user()