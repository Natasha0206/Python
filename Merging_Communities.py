import sys
from collections import deque

N, Q = map(int,input().strip().split(' '))

s = [i for i in range(N+1)]
cnt = [0]+[1 for i in range(N)]

for i in range(Q):
    inpt = input().strip().split(' ')
    qry = inpt[0]
    a = sorted(map(lambda x: int(x),inpt[1:]))
    i0 = a[0]
    if qry == 'M' and s[i0] != s[a[1]]:
        i1 = a[1]
        tmp = deque()
        while i0 != s[i0]:
            tmp.append(i0)
            i0 = s[i0]
        while i1 != s[i1]:
            tmp.append(i1)
            i1 = s[i1]
        if s[i0] != s[i1]:
            cnt[s[i0]] += cnt[s[i1]]
            tmp.append(i1)
            for ix in tmp:
                s[ix] = s[i0]
    elif qry == 'Q':
        tmp = deque()
        while i0 != s[i0]:
            tmp.append(i0)
            i0 = s[i0]
        for ix in tmp:
            s[ix] = s[i0]
        print(cnt[i0])