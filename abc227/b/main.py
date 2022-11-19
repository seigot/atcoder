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

# A,B=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
N = int(input())
S = list(map(int, input().split()))

def check(val):
    for aa in range(1, 350):
        for bb in range(1, 350):
            tmp = 4*aa*bb + 3*aa + 3*bb
            if tmp == val:
                #print(val, aa, bb)
                return True
    return False

cnt = 0
for s in S:
    ret = check(s)
    if ret == False:
        cnt+=1
print(cnt)