n = int(input("Enter a number:"))
sum_even = sum_odd = 0
for i in range(1,n+1):
    if i % 2 == 0:
        sum_even+=i
    if i%2 != 0:
        sum_odd += i
print(sum_even)
print(sum_odd)