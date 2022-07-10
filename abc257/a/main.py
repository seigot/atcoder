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

N,X=map(int, input().split())

base="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
idx = ((X-1)//N)%26
print(base[idx])

#base="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#s=""
#for i in base:
#    s = s + i * N
#print(s[X-1])

#base="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#for i in base:
#    print(i)

#S = "1111111111"
#print(S.count("1"))
#print(S[0:5].count("1"))
#tx = 5
#print(S[0:tx].count("1"))
#print(S[tx:10].count("1"))
#print(S[0:1].count("1"))
#print(S[0:len(S)].count("1"))
