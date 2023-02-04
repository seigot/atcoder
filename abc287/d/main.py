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

S=input()
T=input()
#print(S,T)
lenS = len(S)
lenT = len(T)
offset = lenS - lenT
prev = False

# x = 0
l = [False] * lenT
for ti in range(lenT):
    if S[offset+ti] == T[ti] or (S[offset+ti] == "?" or T[ti] == "?"):
        l[ti] = True
print("Yes") if all(l) else print("No")
# trueの数
trueCnt = 0
for ti in range(lenT):
    if l[ti] == True:
        trueCnt += 1

# x = 1~|T|
# 差分をとる
for x in range(1,lenT+1):
    ti = x-1
    if S[ti] == T[ti] or (S[ti] == "?" or T[ti] == "?"):
        if l[ti] != True:
            trueCnt += 1
        l[ti] = True
        print("Yes") if trueCnt == lenT else print("No")
    else:
        if l[ti] != False:
            trueCnt -= 1
        l[ti] = False
        print("No")  
