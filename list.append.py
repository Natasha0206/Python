# you are given a list n=[1,2,3,4]
#create a new list which contains only the even
#numbers from the list 'n' and print both the lists

n=list([1,2,3,4])
newlist=[]
for i in n:
    if i%2==0:
        newlist.append(i)
print(newlist)
print(n)
