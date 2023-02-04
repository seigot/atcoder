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

S=input()                          # (3)文字列が1つ 入力例:S 

if len(S) != 8:
    print("No")
    exit()
if S[0].isupper() == False:
    print("No")
    exit()
if S[-1].isupper() == False:
    print("No")
    exit()
try:
    val = int(S[1:-1])
except:
    print("No")
    exit()
if val < 100000:
    print("No")
    exit()
print("Yes")

#print(S[0])
#print(S[-1])
#print(S[1:-1])
#print(int(S[1:-1]))


