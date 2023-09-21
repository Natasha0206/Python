x=int(input("Enter the 1st number:"))
y=int(input("Enter the 2nd number:"))
z=int(input("Enter the 3rd number:"))

SUM1 = x+y+z
print(SUM1)

SUM2 = x+y+z
if x==y and x==z:
    print(0)
if x==y and x!=z:
    print(z)
if x==z and x!=y:
    print(y)
if y==z and y!=x:
    print(x)
if x!=y and x!=z and y!=z:
        print(SUM2)
