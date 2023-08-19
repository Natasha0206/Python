# importing the groupby method
from itertools import groupby

# using for loop to iterate through the string
for k, c in groupby(input()):
        
    #printing the output
    print("(%d, %d)" % (len(list(c)), int(k)), end=' ')

