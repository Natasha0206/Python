from textwrap import wrap

def merge_the_tools(string, k):
    ls = wrap(string, k)
    for x in ls:
        result = x[0]
        for i in range(1,k): # k = len(x)
            if x[i] not in result:
                result += x[i]
            else: 
                continue
        print(result)
 

