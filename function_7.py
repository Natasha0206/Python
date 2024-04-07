# take number user input and print its table using function



def table():
    number = int(input("Enter a number:"))
    for i in range(number,number*10+1,number):
        print(i)
table()