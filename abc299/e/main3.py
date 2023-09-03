import sys
sys.setrecursionlimit(5*10**5)
input = sys.stdin.readline
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush
from bisect import bisect_left, bisect_right
from math import gcd
n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

k = int(input())
pd = [list(map(int, input().split())) for i in range(k)]

color = [1]*(n+1) # 頂点 i を黒で塗るとき 1 、白で塗るとき 0 である。
                  # 初めは全てを黒(1)とする
def bfs(s, d):
    que = deque([s])
    depth = [-1]*(n+1)
    depth[s] = 0
    flg = 0
    # 頂点sから距離dまでの頂点を全て探索する。条件に合致しているか確認する。
    while que:
        crr = que.popleft()
        if depth[crr] < d:
            color[crr] = 0 # 頂点sからの距離がdより小さい頂点は全て白(0)にする
        if depth[crr] == d:
            flg |= (color[crr] == 1) # 距離がdの頂点が黒(1)のものが1つでもあればOK
                                     # 1つもない場合は(flg==False)となり条件を満たさない
        if depth[crr] >= d:
            continue       # 距離dより大きいものは無視
        for nxt in graph[crr]:
            if depth[nxt] == -1:
                # 未探索の頂点を探索する
                depth[nxt] = depth[crr]+1
                que.append(nxt)
    return flg

# 2回全探索しておくと重複がない
for i in range(k):
    bfs(*pd[i])
for i in range(k):
    bfs(*pd[i])
ans = 1
for i in range(k):
    ans &= bfs(*pd[i])

if ans:
    print('Yes')
    print(*color[1:], sep = "")
else:
    print('No')

