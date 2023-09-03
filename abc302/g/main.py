import sys
sys.setrecursionlimit(5*10**5)
input = sys.stdin.readline
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush
from bisect import bisect_left, bisect_right
from math import gcd
from itertools import permutations

n = int(input())
a = list(map(int,input().split()))
aa = sorted(a)
d = defaultdict(int)

for i in range(n):
    d[(a[i], aa[i])] += 1

# グラフの自己ループを探す
# グラフのサイズ2のサイクルをとる
# グラフのサイズ3のサイクルをとる
# グラフのサイズ4のサイクルをとる

k = d.keys()
ans = 0
for a,b in list(k):
    if a == b: continue
    v1 = d[(a,b)]
    v2 = d[(b,a)]
    tmp = min(v1,v2)
    ans += tmp
    d[(a,b)] -= tmp
    d[(b,a)] -= tmp

for x in [1,2,3,4]:
    for y in [1,2,3,4]:
        for z in [1,2,3,4]:
            if not (x != y and y != z and z != x):
                continue
            a,b,c = d[(x,y)], d[(y,z)], d[(z,x)]
            tmp = min(a,b,c)
            ans += 2*tmp
            d[(x,y)] -= tmp
            d[(y,z)] -= tmp
            d[(z,x)] -= tmp


for w in [1,2,3,4]:
    for x in [1,2,3,4]:
        for y in [1,2,3,4]:
            for z in [1,2,3,4]:
                if len(set([w,x,y,z])) != 4:
                    continue
                s,t,u,v = d[(w,x)], d[(x,y)], d[(y,z)], d[(z,w)]
                tmp = min(s,t,u,v)
                ans += 3*tmp
                d[(w,x)] -= tmp
                d[(x,y)] -= tmp
                d[(y,z)] -= tmp
                d[(z,w)] -= tmp

print(ans)