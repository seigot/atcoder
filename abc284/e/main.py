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
#    u -= 1
#    v -= 1
    gh[u].append(v)
    gh[v].append(u)

# 深さ幅優先探索
svisit = set()
def dfs(n):
    num = 1
    q = deque()
    q.appendleft(~n)
    q.appendleft(n)
    while q:
        tx = q.popleft()
        svisit.add(tx)
        if tx >= 0:
            for dx in gh[tx]:
                if dx in svisit:
                    # already visited
                    continue
                # not visited
                q.appendleft(~dx)
                q.appendleft(dx)
                num += 1
                if num >= 10**6:
                    print(num)
                    exit()
        else:
            tx = ~tx
            svisit.discard(tx)
    return num

# graph (N頂点M辺)
N,M=map(int, input().split())
gh = [[] for _ in range(N)] 
for ii in range(M):
    u,v=map(int, input().split())
    u -= 1  # 0-indexの場合/1-indexの場合は不要
    v -= 1  # 0-indexの場合/1-indexの場合は不要
    gh[u].append(v)
    gh[v].append(u)
    
# 全頂点で探索
ans = dfs(1)
print(ans)