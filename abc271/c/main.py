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
N=int(input()) 
an=list(map(int, input().split()))
an.sort()

# https://atcoder.jp/contests/abc271/tasks/abc271_c
# 二分探索
upper = N+1 #3*(10**5)
lowwer = 0

d = defaultdict(int)
for ii in range(len(an)):
    nn = an[ii]
    d[nn] += 1
    #print(d)

def func(n):
    # nより大きいものは全て売る
    # 2冊以上あるものは全て売る
    #print("--",n)

    remain = 0
    ans_d = defaultdict(int)
    for ii in d.keys():
       #print(ii,d[ii])
        nn = d[ii]
        # nより大きいものは全て売る
        if ii > n:
            remain += d[ii]
            continue
        # 2冊以上あるものは全て売る
        if nn >= 2:
            remain += nn - 1
            ans_d[ii] += 1
            continue
        ans_d[ii] += 1
    #print(n, remain, ans_d)

    ans = 0
    for ii in range(1, N+1):
        if ans_d[ii] == 1:
            ans += 1
        else:
            # できるだけ買う
            if remain >= 2:
                remain -= 2
                ans += 1
            else:
                break

    # n個買えるならTrue、そうでないならFalse
    if ans >= n:
        return True
    else:
        return False    

while (upper-lowwer)>1:
    n = (upper+lowwer)//2
    ret = func(n)
    if ret == True:
        lowwer = n
    else:
        upper = n

print(lowwer)
