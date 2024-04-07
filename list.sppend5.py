# you are given a list a=[1,2,3,4,5,6] 
# change all the even numbers to 'even' and print the list

a=list([1,2,3,4,5,6])
for i in a:
    if i%2==0:
        i = 'even'
    print(i)