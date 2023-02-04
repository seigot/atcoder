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

H,M=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B

H2 = str(H)
if len(H2) == 1:
    H2 = "0" + H2
M2 = str(M)
if len(M2) == 1:
    M2 = "0" + M2

#print(H2,M2)
def funcprint(h,m):
    if h == "00":
        h = "0"
    if m == "00":
        m = "0"
    print(h,m)

if int(H2[0]) == 0 or int(H2[0]) == 1:
    # func
    if int(H2[1]) >= 6:
            H2 = str((((H//10)+1)*10)%24)
            funcprint(H2,0)
            exit()

if int(H2[0]) == 2:
    if int(M2[0]) >= 4:
            H2 = str((H+1)%24)
            funcprint(H2,0)
            exit()

funcprint(H2, M2) 


