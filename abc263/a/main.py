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
d = defaultdict(int)

cards = list(map(int, input().split()))

for card in cards:
    d[card] += 1

ans="Yes"
for c in cards:
    if d[c] != 2 and d[c] != 3:
        ans="No"
print(ans)