#take a number as user input and print its table using while loop

num = int(input("Enter a number:"))
num1 = 0

while num1 < num*10:
    num1 += num
    print(num1)