# print odd numbers from 1-10 using while loop

num = 1
while num < 10:
    print(num)
    num+=2

# print even numbers from 1-10 using while loop

num = 0
while num < 10:
    print(num)
    num+=2

# using while loop on numbers ranging from 1-10,
#print if number is odd or even

num = 0
while num < 10:
    num += 1
    if num%2 == 0:
        print("even",num)
    else:
        print("odd",num)