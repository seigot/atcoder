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
A = list(map(int, input().split()))

# 1.先頭から探索して単調減少となっている部分の１つ手前のindexを見つける
# 2.単調減少となっている部分以降の中から辞書順で１つ前の数値を見つける
# 3.1.で見つけた数値と置き換えて、後は降順で並び替える

# 1.
prev_a = A[0]
tgt_idx = N-1
tgt_val = A[tgt_idx]
for ii in range(1, N):
    if prev_a > A[ii]:
        tgt_idx = ii - 1
        tgt_val = A[tgt_idx]
    prev_a = A[ii]
#print(tgt_idx, tgt_val)

# 2.
tgt_idx2 = tgt_idx
tgt_val2 = tgt_val
v = 0
for ii in range(tgt_idx+1, N):
    if tgt_val - A[ii] >= 0 and A[ii] > v:
        tgt_idx2 = ii
        tgt_val2 = A[ii]
        v = A[ii]
#print(tgt_idx2, tgt_val2)

# 3.
A[tgt_idx] = tgt_val2
A[tgt_idx2] = tgt_val
_A = A[tgt_idx+1:N]
_A.sort(reverse=True)
__A = A[:tgt_idx+1] + _A 
print(*__A)
