for n in range(15,26):
    for i in range(2,n):
        if n%i==0:
            print("Not a prime",n)
            break
    else:
        print("It is prime",n)
       