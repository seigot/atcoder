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

from itertools import repeat, takewhile
from math import inf
import sys
sys.setrecursionlimit(10 ** 7)

n = int(input())                           # 頂点の数
d = list(map(int, input().split()))        # dのリスト
deg = [0] * n                              # 各頂点の辺の数
g = tuple(list() for _ in repeat(None, n)) # 各頂点から繋がっている辺と辺の重み

# グラフを作成する
for _ in repeat(None, n - 1):
    u, v, w = map(int, input().split())
    # 0-index
    u -= 1
    v -= 1
    g[u].append((v, w))
    g[v].append((u, w))
    deg[u] += 1
    deg[v] += 1
#print(g)
dq = deque(v for v in range(n) if deg[v] == 1) # 1つしか辺がないもの
eq = [None] * n                                # eq 
less = [None] * n                              # less 
#print(dq)
#print(eq)
#print(less)
while dq:

    # 対象の頂点を選ぶ
    v = dq.popleft()
    # 対象の頂点に繋がる辺の重み計算用リスト
    edges = []

    # baseを求める, baseとは
    base = 0
    for u, w in g[v]:                     # vに繋がる辺と重みに着目する
        if eq[u] is None:  # 新規
            deg[u] -= 1
            if deg[u] == 1:
                dq.append(u)              # 次に探索する対象（葉）の追加
            continue
        base += eq[u]                     # 自分の子
        edges.append(less[u] + w - eq[u]) # 重みを追加

    if d[v] == 0:               # 0の場合
        eq[v] = base            # 0の場合はエッジを選択できない
        less[v] = -inf          # 0の場合はエッジを選択できない
    else:
        # d=0以外の場合は大きいものから順番にMax d個まで(だたし値が正のもの)辺を取り出す操作を行う
        edges.sort(reverse=True)                                           # takewhileを使うために降順ソート
        eq[v] = base + sum(takewhile(lambda e: e > 0, edges[:d[v]]))       # edgesの0以上の辺を出力して合計値を返す
        less[v] = base + sum(takewhile(lambda e: e > 0, edges[:d[v] - 1])) # edgesの0以上の辺を出力して合計値を返す

print(eq[v])  # 最後の頂点=根
