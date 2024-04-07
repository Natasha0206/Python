# you are given 2 lists n=[1,2,3] and m=[4,5,6] and create a new lists whose
#elements are the sum of elements of lists n and m at position 'i'

# for example-
# at index 0, n[0] = 1, m[0] = 4
# so, k[0] = 1+4 = 5

n=list([1,2,3])
m=list([4,5,6])
k=[]
j=0
for i in range (len(n)):
    sum = n[i]+m[j]
    k.append(sum)
print(k)