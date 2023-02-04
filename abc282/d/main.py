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

n,m = map(int,input().split())
graph = [[] for i in range(n+1)]
d = [0]*(n+1)
for i in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)
  # 数を数える
  d[a] += 1
  d[b] += 1

# 2部グラフかどうかの判定
depth = [-1]*(n+1) # 色
ans = 0
all = []
flg = 1
# 各頂点を探索対象に含める、グラフ毎に探索する
for i in range(1,n+1):
  if depth[i] != -1:
    # 探索済みであればスキップ
    continue
  depth[i] = 0
  que = deque([i])
  g = [[],[]]

  # 幅優先探索
  while que:
    crr = que.popleft()
    g[depth[crr]].append(crr)   # gに現在の頂点を加える

    for nxt in graph[crr]:
      if depth[nxt] == -1:
        # 次の点が未探索である場合は探索対象にする
        depth[nxt] = (depth[crr]+1)%2  # 色を塗る
        que.append(nxt)                # 次の探索対象を加える
      if depth[nxt] == depth[crr]:
        # 現在の頂点の色と次の頂点の色が異なる場合は２部グラフではないと判定する
        flg = False
  all.append(g)

if not flg:
  # 2部グラフではない場合は"0"を出力する
  print(0)
  exit()

# 2部グラフの場合は数を数える
# グラフは１つではない場合があるのでそれぞれのグラフごとに数える
for a,b in all:
  # a : 白(0)
  # 白(0)に着目した時に、条件に合う２部グラフの数を数える
  aa = len(a)
  for ai in a:
    # 繋げることが可能な頂点の数を加算する、各グラフ毎に考える
    # (全頂点の数-白の数-黒のうちaiに繋がっている頂点の数)
    ans += n - aa - d[ai]
  # b : 黒(1)
  # 黒(1)に着目した時に、条件に合う２部グラフの数を数える
  bb = len(b)
  for bi in b:
    ans += n - bb - d[bi]
print(ans//2)
