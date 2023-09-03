#https://atcoder.jp/contests/ABC315/tasks/ABC315_e 
import sys
sys.setrecursionlimit(5*10**5)
input = sys.stdin.readline
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush
from bisect import bisect_left, bisect_right
from math import gcd


n = int(input())
l = [-1] + [list(map(int,input().split())) for i in range(n)]

need = set()
d = [-1]*(n+1)

que = [1]
d[1] = 0
# 必要な頂点を取得する
while que:
    crr = que.pop()
    need.add(crr)
    for nxt in l[crr][1:]:
        if d[nxt] != -1: continue
        d[nxt] = 0
        que.append(nxt)

# 頂点の数を数える
indeg = [0]*(n+1)
for i in need:
    for nxt in l[i][1:]:    
        indeg[nxt] += 1

# BFS、頂点の数をカウントして最後に登場した頂点から探索する（帰りがけ順になる）
que = deque([1])
ord = []
while que:
    crr = que.popleft()
    ord.append(crr)
    for nxt in l[crr][1:]:
        indeg[nxt] -= 1
        if indeg[nxt] == 0:
            que.append(nxt)

print(*ord[1:][::-1])
