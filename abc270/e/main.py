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
N,K=map(int, input().split())
A=list(map(int, input().split()))



def is_over_K(loopn):
    sum = 0
    for ii in range(N):
        sum += min(loopn, A[ii])
    if sum > K:
        return True
    else:
        return False

# 必要な周回数を二分探索で求める
loopn = 0
upper = K
lowwer = 0
while upper - lowwer > 1:
    middle = (upper + lowwer)//2
    ret = is_over_K(middle)
    #print("ret", middle, ret)
    if ret == False:
        lowwer = middle
    else:
        upper = middle
loopn = lowwer
#print("loopn", loopn)

# 周回数分のループを回した後の個数を計算する
remain = K
for ii in range(N):
    val = min(loopn, A[ii])
    A[ii] -= val
    remain -= val

# 周回数の端数を計算する
#print("remain", remain)
for ii in range(N):
    if remain == 0:
        break
    if A[ii] >= 1:
        A[ii] -= 1
        remain -= 1

# 数を出力する
print(*A)
