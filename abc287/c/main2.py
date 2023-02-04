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

# graph (N頂点M辺)
N,M=map(int, input().split())
gh = [[] for _ in range(N)] 
for ii in range(M):
    u,v=map(int, input().split())
    u -= 1  # 0-indexの場合/1-indexの場合は不要
    v -= 1  # 0-indexの場合/1-indexの場合は不要
    gh[u].append(v)
    gh[v].append(u)

# 1.次数1の頂点を見つける
# 2.次数1の頂点からパスを辿る

# 1.次数1の頂点を見つける
tx = -1
for ii in range(N):
    if len(gh[ii]) == 1:
        tx = ii
if tx == -1:
    print("No")
    exit()

#print("tx",tx)
# 2.次数1の頂点からパスを辿る
# 幅優先探索
dq = deque()
s = set()
dq.append(tx)
s.add(tx)
while dq:
    tx = dq.popleft()
    cnt = 0
#    print("tx",tx)

    for dx in gh[tx]:
        if dx not in s:
            if cnt >= 1:
                print("No")
                exit()
            cnt += 1
            dq.append(dx)
            s.add(dx)
#print(len(s),N)
if len(s) == N:
    print("Yes")
else:
    print("No")
