# you have a list a=[1,2,3,4,5,6,7,8] print the sum of all even and all odd numbers
a = list([1,2,3,4,5,6,7,8])
sum_even = 0
sum_odd = 0
for i in a:
    if i%2==0:
        print("even",i)
        sum_even += i
        
    else:
        print("odd",i)
        sum_odd += i
print("sum of odd Numbers:",sum_odd)
print("sum of even Numbers:",sum_even)