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
from itertools import permutations,combinations
from copy import deepcopy
dpos2 = ((1, 0), (0, 1))
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos4cross = ((1, 1), (1, -1), (-1, 1), (-1, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

H,W=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
C = [list(input()) for h in range(H)] # maze(###.###) のようなスペースなしの2次元配列で受け取り
#print(C)

# Xのカウント
cnt_x = defaultdict(int)
N=min(H,W)
for j in range(H):
    for i in range(W):
        tx = C[j][i]
        #print(i,j,tx)
        if tx == "#":
            # (i,j)が"#"の場合は周囲を探索する
            cnt = 0
            flag = False
            for n in range(1,N+1):
                for d in dpos4cross:
                    dx = i + d[0]*n
                    dy = j + d[1]*n
                    if dx < 0 or dx >= W or dy < 0 or dy >= H:
                        flag = True
                        break
                    if C[dy][dx] == ".":
                        flag = True
                        break
                    cnt += 1
                if flag == True:
                    break
            cnt_x[cnt//4] += 1
#            print(i,j,tx, n, cnt, cnt_x[n])
l = []
for i in range(1,N+1):
    l.append(cnt_x[i])
print(*l)
