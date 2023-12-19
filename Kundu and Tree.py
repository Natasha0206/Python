def find(x):
    while uf[x] >= 0:
        if uf[uf[x]] >= 0:
            uf[x] = uf[uf[x]]
        x = uf[x]
    return x

n = int(input())
uf = [-1]*n
for i in range(n-1):
    x, y, col = input().split()
    if col == 'b':
        x, y = find(int(x)-1), find(int(y)-1)
        if uf[x] > uf[y]:
            x, y = y, x
        uf[x] += uf[y]
        uf[y] = x
a, b, c = 0, 0, 0
for i in range(n):
    if uf[i] < 0:
        c -= b*uf[i]
        b -= a*uf[i]
        a -= uf[i]
print(c % int(1e9+7))