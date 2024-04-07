# you are given a list n=[1,2,3,4,5,6,7,8,9], create two new lists which contain all the even and odd numbers from 'n' respectively. remove the maximum element from both the list then print the sum of all elements of both the lists as
# even : 'SUM'
# odd : 'SUM'

n=list([1,2,3,4,5,6,7,8,9])
e = []
o = []
sum = 0
for i in range(len(n)):
    if n[i]%2 == 0:
        e.append(n[i])
    else:
        o.append(n[i])
e.remove(max(e))
o.remove(max(o))      
print(e)
print(o)
x = sum(e)
y = sum(o)
print(x)
print(y)