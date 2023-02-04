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
gh = [[] for _ in range(N+1)] 
for ii in range(M):
    u,v=map(int, input().split())
    gh[u].append(v)
    gh[v].append(u)
#print(gh)

# BFS
visitedall = set()
visited = set()
closedloop = set()
def bfs(tx):
    dq = deque()
    dq.append((tx,0))
    cnt = 0
    while dq:
        tx, pre = dq.popleft()
        if tx > 0:
            if tx in visited:
                continue
            visited.add(tx)
            for dx in gh[tx]:
                if dx == pre:
                    # skip
                    continue
                if dx not in visited:
                    # 未探索
#                   dq.appendleft((~dx,0))
                    dq.appendleft((dx,tx))
                else:
                    # 閉路
                    if ((tx,dx) not in closedloop) and ((dx,tx) not in closedloop):
                        closedloop.add((tx,dx))
#        else:
#            tx = ~tx
#            visited.discard(tx)
for ii in range(1,N+1):
    bfs(ii)
print(len(closedloop)) 




