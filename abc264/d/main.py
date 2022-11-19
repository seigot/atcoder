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
S = list(input())
atcoder = list("atcoder")

ans = 0
for tc in atcoder:
    for ii in range(len(S)):
        if S[ii] == tc:
            ans += ii
            S.remove(tc)
            break
print(ans)
