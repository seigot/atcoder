#!/usr/bin/env python3
import sys
sys.setrecursionlimit(4100000)
import math
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
from heapq import heapify, heappush, heappop
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

#N=int(input())                     # (1)数字が1つ 入力例:N
N,M,K=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
UVA = list()
for ii in range(M):
    u,v,a=map(int, input().split()) 
    UVA.append((u,v,a))
S = set(map(int, input().split()))
gh = defaultdict(set)

# 1.Graph G''を作成する
#   (a, 0): switchがOFFになっている状態
#   (a, 1): switchがONになっている状態
# 2.ダイクストラ法 or 01BFSで探索する

# 1.
for ii in range(M):
    u,v,a = UVA[ii]
    gh[u].add((v,a))
    gh[v].add((u,a))
#    # スイッチがある場合(最初から入れる場合は頂点ありすぎてTLEになる)
#    if u in S:
#        gh[(u,1)].add((u,0))
#        gh[(u,0)].add((u,1))
#    if v in S:
#        gh[(v,1)].add((v,0))
#        gh[(v,0)].add((v,1))

# 2.
dq = list()
#dist = defaultdict(lambda: INF)
visited = set()
heapify(dq)

def _01bfs(sx):

    ddist = 0
    heappush(dq, [ddist,sx,1])
    visited.add(((sx,1)))

    # bfs
    while dq:
        tdist, tx, tsw = heappop(dq)
#        print(tdist,tx,tsw)

        # switch
        if tx in S:
            ddist = tdist
            dx = tx
            dsw = tsw^1
            if (dx,dsw) not in visited:
                heappush(dq, [ddist,dx,dsw])
                visited.add((dx,dsw))
        # 移動
        for nx in gh[tx]:
            ddist = tdist + 1
            dx = nx[0]
            dsw = nx[1]
            if dsw != tsw: 
                continue
            # Nにいるかどうかチェック
            if dx == N:
                print(ddist)
                exit()
            # 未探索の場合は探索候補にする（heapqを用いており未探索=探索すべき頂点であることを保証している）
            if (dx,dsw) not in visited:
                heappush(dq, [ddist,dx,dsw])
                visited.add((dx,dsw))

_01bfs(1)
print(-1)
