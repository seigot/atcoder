#!/usr/bin/env python3                                                                          
import sys
input = sys.stdin.readline
sys.setrecursionlimit(4100000)
import math
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush
from math import gcd
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

#N=int(input())                     # (1)数字が1つ 入力例:N
#A,B=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
#S=input()                          # (3)文字列が1つ 入力例:S 
#S,T=map(str, input().split())      # (4)文字列が2つ以上で別々に受け取り 入力例:S T
#A=list(map(int, input().split()))  # (5)リストで受け取り 入力例:A1 A2 ... An
#A = deque(map(int, input().split()))  # (6)dequeueで受け取り 入力例:A1 A2 ... An
#maze = [list(input()) for h in range(H)] # maze(###.###) のようなスペースなしの2次元配列で受け取り
#P=[list(map(int, input().split())) for h in range(H)] # 1 2 3 4 のようなスペースありの2次元配列を受け取り

# graph (N頂点M辺)
N,M=map(int, input().split())
gh = [[] for _ in range(N)] 
for ii in range(M):
    u,v=map(int, input().split())
    u -= 1  # 0-indexの場合/1-indexの場合は不要
    v -= 1  # 0-indexの場合/1-indexの場合は不要
    gh[u].append(v)
    gh[v].append(u)
#print(gh)

# bfs
visited = set()
def bfs(n):

    Nnodes = set()
    Nedges = []
    Nnodes.clear()
    Nedges.clear()

    q = deque()
    q.append(n)
    visited.add(n)
    Nnodes.add(n)
    while q:
        tx = q.popleft()
#        print(gh[tx])
        for dx in gh[tx]:
            # edge count
            pair = (tx,dx) if tx < dx else (dx,tx)
            Nedges.append(pair)

            if dx in visited:
                # already visited
                continue
            # not visited
            q.append(dx)
            visited.add(dx)
            Nnodes.add(dx)

#    print(Nnodes)
#    print(Nedges)
    return len(Nedges)//2 == len(Nnodes)

for ii in range(0,N):
    if ii in visited:
        continue
    ret = bfs(ii)
    if ret == False:
        print("No")
        exit(0)
print("Yes")
