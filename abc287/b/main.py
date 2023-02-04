#!/usr/bin/env python3
import sys
sys.setrecursionlimit(4100000)
import math
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N,M=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
sl = []
for ii in range(N):
    S=input()                          # (3)文字列が1つ 入力例:S 
    sl.append(S[-3:])

ans = 0
tl = []
for ii in range(M):
    T=input()
    tl.append(T)

ans = 0
for ii in range(N):
    for jj in range(M):
        if sl[ii] == tl[jj]:
            ans += 1
            break
print(ans)
