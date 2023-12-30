from array import array
from bisect import bisect_right

t = int(input())
for _ in range(t):
    n = int(input())
    arr = array('I', [int(i) for i in input().split()])
    sarr = array('I', [arr[0]])
    result = 0
    for i in range(1, n):
        e = arr[i]
        j = bisect_right(sarr, e)       
        sarr.insert(j, e)
        result += i - j
    print(result) 