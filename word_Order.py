from collections import Counter
n = int(input())
l1 = [input().strip() for _ in range(n)]
res = Counter(l1)
print(len(res))
print(*res.values())
