# you are given a list n=[1,2,3,4,5,6,7,8] 
#print all the even numbers, else print 'meh'

n = list([1,2,3,4,5,6,7,8])
for i in n:
    if i%2==0:
        print(i)
    else: 
        print("meh")