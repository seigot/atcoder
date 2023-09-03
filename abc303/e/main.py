#!/usr/bin/env python3                                                                          
import sys
input = sys.stdin.readline # 文字列Sの場合は最後に"¥n"が付くので注意
sys.setrecursionlimit(4100000)
import math
import os
from inspect import currentframe
ONLINE_JUDGE = os.environ["HOME"] == "/home/contestant"
def error1(*args, end="\n"): # 変数のみ表示
    if ONLINE_JUDGE: return
    print("[stderr]", *args, end=end, file=sys.stderr)
def error(*args): # 変数の名前と値をまとめて表示
    if ONLINE_JUDGE: return
    names = {id(v): k for k, v in currentframe().f_back.f_locals.items()}
    print("[stderr]",' '.join([names.get(id(arg), '???') + ' = ' + repr(arg) for arg in args]), file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush
from math import gcd
from itertools import permutations,combinations
from copy import deepcopy
dpos2 = ((1, 0), (0, 1))
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos4cross = ((1, 1), (1, -1), (-1, 1), (-1, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
MOD = 998244353
def invmod(a):
    return pow(a,-1,MOD)
INF = float("inf")
MINF = -float("inf")

N=int(input())                     # (1)数字が1つ 入力例:N
#A,B=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
#S=input()                          # (3)文字列が1つ 入力例:S 
#S,T=map(str, input().split())      # (4)文字列が2つ以上で別々に受け取り 入力例:S T
#A=list(map(int, input().split()))  # (5)リストで受け取り 入力例:A1 A2 ... An
#A = deque(map(int, input().split()))  # (6)dequeueで受け取り 入力例:A1 A2 ... An
#maze = [list(input()) for h in range(H)] # maze(###.###) のようなスペースなしの2次元配列で受け取り
#HW=[list(map(int, input().split())) for h in range(H)] # 1 2 3 4 のようなスペースありの2次元配列を受け取り, HW[ty][tx]

# graph (N頂点M辺)
gh = [[] for _ in range(N)] 
for ii in range(N-1):
    u,v=map(int, input().split())
    u -= 1  # 0-indexの場合/1-indexの場合は不要
    v -= 1  # 0-indexの場合/1-indexの場合は不要
    gh[u].append(v)
    gh[v].append(u)
error(gh)

ans = []
visited = defaultdict(int)
# 1.頂点を１つ探索する（葉を見つけた先次数2のもの）
for ii in range(N):
    if len(gh[ii]) == 1:
        # 頂点
        tx = gh[ii][0]
        break
error(tx)

# 2.頂点を基準にBFSして距離を求める
# 幅優先探索
# (gh:グラフ)
# s: 初めの頂点番号
# n: 頂点数
# sから全頂点への距離を求める
# return
#  depth: 距離(list) もし辿り着けない頂点がある場合は-1をいれる
#  pre:   探索前の頂点番号(list)
def bfs(s, n):
    que = deque([s])
    depth = [-1]*(n+1)
    pre = [-1]*(n+1)
    depth[s] = 0
    while que:
        crr = que.popleft()
        error(que,crr)
        for nxt in gh[crr]:
            if depth[nxt] == -1:
                depth[nxt] = depth[crr]+1
                pre[nxt] = crr
                que.append(nxt)
    return depth, pre
d, _ = bfs(tx, N)
error(d)

# 3.距離が3の倍数である頂点の次数を求めてソートする
ans = []
for ii in range(N):
    if d[ii]%3 == 0:
        error(ii)
        tx = len(gh[ii])
        ans.append(tx)

ans = sorted(ans)
print(*ans)
