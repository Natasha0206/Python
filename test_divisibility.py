a=float(input("Enter the 1st number:"))
b=float(input("Enter the 2nd number:"))
c=float(input("Enter the 3rd number:"))
d=float(input("Enter the 4rd number:"))
e=float(input("Enter the 5rd number:"))
div = float(input("Enter the Divisor:"))
count=0
if a%div==0:
    print("It is divisible by :",a)
    count = count + 1
if b%div==0:
    print("It is divisible by :",b)
    count = count + 1
if c%div==0:
    print("It is divisible by :",c)
    count = count + 1
if d%div==0:
    print("It is divisible by :",d)
    count = count + 1
if e%div==0:
    print("It is divisible by :",e)
    count = count + 1
print("Total numbers of divisor:",count)



