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
#N,M=map(int, input().split())
#gh = [[] for _ in range(N)] 
#for ii in range(M):
#    u,v=map(int, input().split())
#    u -= 1  # 0-indexの場合/1-indexの場合は不要
#    v -= 1  # 0-indexの場合/1-indexの場合は不要
#    gh[u].append(v)
#    gh[v].append(u)
# 2次元配列
#dp = [[0]*(n+1) for _ in range(n+1)]
# 3次元配列
#dp = [[[0]*(n+1) for _ in range(n+1)] for _ in range(n+1)]
