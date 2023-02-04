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

N=int(input())                     # (1)数字が1つ 入力例:N
l = []
for ii in range(N):
    S=input()
    l.append(S)

# 辞書順でソート
import copy
ll = copy.deepcopy(l)
l.sort()
l.insert(N,"0")
l.insert(0,"0")
#print(l)

# 前後関係を見る
d = defaultdict(int)
for ii in range(1,N+1):
    ans = 0
    # 前
    n = min(len(l[ii-1]), len(l[ii]))
    cnt = 0
    for jj in range(n):
        if l[ii-1][jj] != l[ii][jj]:
            break
        cnt += 1
    ans = max(ans, cnt)

    # 後
    n = min(len(l[ii+1]), len(l[ii]))
    cnt = 0
    for jj in range(n):
        if l[ii+1][jj] != l[ii][jj]:
            break
        cnt += 1
    ans = max(ans, cnt)
    d[l[ii]] = ans

for ii in range(N):
    print(d[ll[ii]])
