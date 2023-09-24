for num in range(15,25):
    for i in range(2,num):
        if num%i==0:
            j=num/i
            print("Found a factor(",i,")for",num)
            break
    else:
        print(num, "is a prime number")
