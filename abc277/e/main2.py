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
#gh = defaultdict(list)
gh = defaultdict(set)
#print(UVA)
#print(S)

# 1.Graph G''を作成する
#   (a, 0): switchがOFFになっている状態
#   (a, 1): switchがONになっている状態
# 2.ダイクストラ法 or 01BFSで探索する

# 1.
for ii in range(M):
    u,v,a = UVA[ii]
    gh[(u,a)].add((v,a))
    gh[(v,a)].add((u,a))
#    # スイッチがある場合
#    if u in S:
#        gh[(u,1)].add((u,0))
#        gh[(u,0)].add((u,1))
#    if v in S:
#        gh[(v,1)].add((v,0))
#        gh[(v,0)].add((v,1))
print(gh)

# 2.
dq = list()
#dist = defaultdict(lambda: INF)
s = set()
heapify(dq)

def _01bfs(sx):

    ddist = 0
#    dq.append((sx,1, ddist))
    heappush(dq, [ddist,sx,1])
 #   dist[(sx,1)] = ddist
    s.add(((sx,1)))

    # bfs
    while dq:
#        print(dq)
        tdist, tx, tsw = heappop(dq)
        for ii in gh[(tx,tsw)]:
            dx = ii[0]
            dsw = ii[1]
            ddist = tdist
            # 距離の更新
            if tx != dx:
                ddist = tdist + 1
                # Nにいるかどうかチェック
                if dx == N:
                    print(ddist)
                    exit()
            ll = []
            if tx in S:
                ll.append(0)
                ll.append(1)
            else:
                ll.append(tsw)
#        gh[(u,1)].add((u,0))
#        gh[(u,0)].add((u,1))
#    if v in S:
#        gh[(v,1)].add((v,0))
#        gh[(v,0)].add((v,1))
            for ii in ll:
#            if ddist < dist[(dx,dsw)]:
                #print(dx, dsw, ii)
                dsw = ii
                print(ddist,dx,dsw)
                if (dx,dsw) not in s:
                # 距離が小さい場合は追加する(先頭に)
#                dist[(dx,dsw)] = ddist
                    s.add((dx,dsw))
                    heappush(dq, [ddist,dx,dsw])


_01bfs(1)
print(-1)
