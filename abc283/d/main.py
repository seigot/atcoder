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

s = set()
dicts = defaultdict(set)

cnt = 0
for si in S:
    if si == "(":
        cnt += 1
    elif si == ")":
        for sii in dicts[cnt]:
            s.remove(sii)
        dicts[cnt].clear()
        cnt -= 1
    else:
        if si in s:
            print("No")
            exit()
        dicts[cnt].add(si)
        s.add(si)
print("Yes")
