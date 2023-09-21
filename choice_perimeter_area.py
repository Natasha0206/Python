r = float(input("Enter radius:"))
print("1. Calculate Area:")
print("2. Calculate Perimeter:")
choice = int (input("Enter your choice(1 or 2):"))
if choice == 1:
    area=3.14*r**2
    print("Area of the circle:",area)
if choice == 2:
    perimeter=(2*3.14)*r
    print("Perimeter of the circle:",perimeter)


