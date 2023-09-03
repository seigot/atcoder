#!/usr/bin/env python3                                                                          
import sys
input = sys.stdin.readline
sys.setrecursionlimit(4100000)
import math
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush
from math import gcd
from itertools import permutations,combinations
from copy import deepcopy
dpos2 = ((1, 0), (0, 1))
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

L,N1,N2=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
dict1 = defaultdict(int)
vl1 = []
indexs1 = []
index_sum1 = 0
dict2 = defaultdict(int)
vl2 = []
indexs2 = [0]
index_sum2 = 0

# input
for ii in range(N1):
    v1,l1=map(int, input().split())
    vl1.append((v1,l1))
    indexs1.append(index_sum1)
    index_sum1 += l1

for ii in range(N2):
    v2,l2=map(int, input().split())
    vl2.append((v2,l2))
    indexs2.append(index_sum2)
    index_sum2 += l2
indexs2.append(L)

# search
ans = 0
for ii in range(N1):
    cidx = indexs1[ii]
    cv,cl = vl1[ii]
    print("cidx", cidx)
    print("cv,cl", cv, cl)
    tidx_base = 0
    if cidx == 0:
        tidx_base = 1
        tidx = 0
    else:
        tidx_base = bisect_right(indexs2, cidx) - 1
        tidx = indexs2[tidx_base]
    print("tidx_base,tidx", tidx_base, tidx)
#    print("tidx", tidx, indexs2[tidx])
    header = 0
    footer = 0
    while tidx <= cidx:
        print("tidx_base,tidx", tidx_base, tidx)
        tv,tl = vl2[tidx_base - 1]
        print("tv,tl,cv,cl", tv,tl,cv,cl)
        # count
        if cv == tv:
            ans += tl
            if tidx < cidx:
                # header
                header = cidx - tidx
            if cidx + cl < tidx + tl:
                # footer
                footer = tidx + tl - (cidx + cl)
        # next
        tidx_base = tidx_base + 1
        tidx += indexs2[tidx_base]
    print(ans, header, footer)
    ans = ans - (header + footer)

print(ans)



print(vl1)
print(indexs1)
print(vl2)
print(indexs2)
