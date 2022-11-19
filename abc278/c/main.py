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

N,Q=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B

# Ti=1 のとき：ユーザーAiがユーザーBiをフォローしたことを表す。
# Ti=2 のとき：ユーザーAiがユーザーBiのフォローを解除したことを表す。
# Ti=3 のとき：ユーザーAiとユーザーBiが互いにフォローしているかをチェックすることを表す。
d = defaultdict(set)
for ii in range(Q):
    t,a,b=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
    if t == 1:
        d[a].add(b)
    if t == 2:
        d[a].discard(b)
    if t == 3:
        if b in d[a] and a in d[b]:
            print("Yes")
        else:
            print("No")
