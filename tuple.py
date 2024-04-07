# Tuple

# you are given a tuple n = (1,2,3,4,5,6,7,8,9)
# replace all the even numbers by adding 1 
# to them and then print the updated tuple

n = (1,2,3,4,5,6,7,8,9)
x = list(n)
for i in range(len(x)):
    if x[i]%2==0:
        x[i] = x[i] + 1
    else:
        continue
print(tuple(x))