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
# https://atcoder.jp/contests/abc273/submissions/35713208
from collections import defaultdict
from bisect import bisect_left
H, W, rs, cs = map(int, input().split())
N = int(input())

C = defaultdict(list)
R = defaultdict(list)
for i in range(N):
    r, c = map(int, input().split())
    R[r].append(c)
    C[c].append(r)
for r in R.keys():
    R[r].sort()
for c in C.keys():
    C[c].sort()

r, c = rs, cs
for _ in range(int(input())):
    d, l = input().split()
    l = int(l)

    def f(X, x, diff, adjust):
        diff = min(diff, l)
        pos = bisect_left(X, x) - adjust
        if 0 <= pos < len(X):
            diff = min(diff, abs(X[pos] - x) - 1)
        return diff

    if d == 'U':
        r -= f(C[c], r, r - 1, 1)
    elif d == 'D':
        r += f(C[c], r, H - r, 0)
    elif d == 'L':
        c -= f(R[r], c, c - 1, 1)
    else:  # d == 'R':
        c += f(R[r], c, W - c, 0)
    print(r, c)
