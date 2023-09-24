import math
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))

if a==0:
    print("should not be zero")
else:
    delta = b*b-4*a*c
    if delta > 0:
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Root1=",root1,",Root2=",root2)

    elif delta == 0:
        root1 = -b/2*a
        print("Root1=",root1,",Root2=",root1)

    else:
        print("Complex and imaginary")


