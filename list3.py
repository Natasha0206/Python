# you have a list n=[1,2,3,4,5,6] if the
#index is even print the element at the
#particular index else print 'odd index'

n=list([1,2,3,4,5,6])
for i in range (len(n)):
    if n[i]%2==0:
        print(n[i])
    else:
        print("odd index")