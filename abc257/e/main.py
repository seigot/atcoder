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

N = int(input())
C = [INF] + list(map(int, input().split()))

# print(N, C)
# 1.できるだけ長く
# 2.余りを使ってできるだけ大きく

# 1.できるだけ長く
# 最小値Cを探す
min_i = 0
min_C = INF
for ii in range(1, len(C)):
    val_C = C[ii]
    if val_C < min_C:
        min_i = ii
        min_C = val_C
# print(min_i,min_C)

ans_length = N // min_C
N_remain = N - (min_C * ans_length)
ans = [min_i] * ans_length
# print(ans, N_remain)

# 2.余りを使ってできるだけ大きく
for ii in range(len(ans)):
    base_i = ans[ii]
    base_C = C[base_i]

    # 現状+余りの範囲で、より大きな数値に置換できるかどうか
    candidate_i = base_i
    candidate_C = base_C
    for jj in range(base_i, len(C)):
        target_i = jj
        target_C = C[target_i]
        if base_C + N_remain >= target_C:
            candidate_i = target_i
            candidate_C = target_C
            #break

    # 置換する
    if candidate_i != base_i:
        ans[ii] = candidate_i
        N_remain -= (candidate_C - base_C)

#val = 0
#for ii in range(len(ans)):
#    val = val*10 + ans[ii]
#print(val)
print("".join(list(map(str, ans))))

