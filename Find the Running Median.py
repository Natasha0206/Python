from heapq import *
under = []
upper = []
N = int(input())
for _ in range(N):
    curNumber = int(input())
    if (len(upper) == 0):
        upper.append(curNumber)
        print(curNumber)
        continue
    middle = upper[0]
    if curNumber >= middle:
        heappush(upper,curNumber)
    else:
        heappush(under, -curNumber)
    if len(under) >= len(upper):
        heappush(upper, -heappop(under))
    if len(upper) >= len(under) + 2:
        heappush(under, -heappop(upper))
    if (len(upper) + len(under)) % 2 == 1:
        print(float(upper[0]))
    else:
        print((float(upper[0]) + -under[0])/2)