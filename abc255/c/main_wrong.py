#!/usr/bin/env python3
import sys
sys.setrecursionlimit(4100000)
import math
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

# 6 2 3 3
#   A D N
#   [2 5 8]
ans = 0
X, A, D, N = map(int,input().split())

S = [A]
# 配列化
for ii in range(N-1):
    num = S[ii] + D 
    S.append(num)
S.sort()

#print(S)
#print(S[0],S[-1])

# 初項より小さい場合
if X <= S[0]:
    ans = S[0] - X
    print(ans)
    exit()
# 末項より大きい場合
if X >= S[-1]:
    ans = X - S[-1]
    print(ans)
    exit()
# 数列の中にある場合
# 二分探索
bl = bisect_left(S, X)
br = bisect_right(S, X)
#print(bl, br, S[bl], S[br])
ll = abs(S[bl-1] - X )
rr = abs(S[br] - X )
ans = min(ll, rr)
print(ans) 