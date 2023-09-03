#!/usr/bin/env python3                                                                          
# https://atcoder.jp/contests/abc292/submissions/39438263

import sys
sys.setrecursionlimit(5*10**5)
input = sys.stdin.readline
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush
from bisect import bisect_left, bisect_right
from math import gcd

n,m = map(int,input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)

# 幅優先探索
def bfs(s):
  cnt = 0
  que = deque([s])
  depth = [-1]*(n+1)
  depth[s] = 0        # スタート地点はdepth=0
  while que:
    crr = que.popleft()
    if depth[crr] >= 2:
      # depth==2以上の頂点を数える
      # a-->b,b-->cの場合はa-->cに有向辺を作成する
      cnt += 1
    for nxt in graph[crr]:
      if depth[nxt] == -1:
        # 未探索である場合は探索する
        depth[nxt] = depth[crr]+1   # スタート地点から1つ先はdepth=1,2つ先はdepth=2
        que.append(nxt)
  return cnt
ans = 0
for i in range(1, n+1):
  # 各頂点について探索する
  ans += bfs(i)

print(ans)