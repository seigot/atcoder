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

# A,B=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B

N = int(input())
l = []
l_ans = []
for ii in range(N):
    L, R = map(int, input().split())
    l.append([L, R])
l.sort()
#print(l)

for ii in range(len(l)):
    tL = l[ii][0]
    tR = l[ii][1]

    if ii == 0:
        l_ans.append([tL,tR])
    else:
        ll = l_ans.pop()
        preL = ll[0]
        preR = ll[1]
        if tL <= preR:
            preR = max(preR, tR)
            l_ans.append([preL,preR])
        else:
            l_ans.append([preL,preR])
            l_ans.append([tL,tR])

for ii in range(len(l_ans)):
    print(l_ans[ii][0], l_ans[ii][1])
