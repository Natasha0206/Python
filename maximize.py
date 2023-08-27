from itertools import product,starmap
from operator import mul

def dotproduct(vec1, vec2):
    "Compute a sum of products."
    return sum(starmap(mul, zip(vec1, vec2)))

K, M = map(int,input().split())
N_list = []


for _ in range(K):
    N_i, N = input().split(" ",1)
    N_list.append(list(map(int,N.split())))
    
max_S = 0
for x in product(*N_list):
   S = dotproduct(x,x)%M
   if S > max_S:
    max_S = S
    
print(max_S)