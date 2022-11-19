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

N, C = map(int, input().split())
X = [(C >> i) % 2 for i in range(30)] # 2進数にする

# 0 -> x = 0
# 1 -> x = 1
# 2 -> xor 1
# 3 -> do nothing

op = [3] * 30

def op_to_new_op(op, t, b):  # 合成関数を求める
    if t == 1 and b == 0: # and 0
        return 0          # and 0の場合は強制的に0に変換する
    if t == 2 and b == 1: # or 1
        return 1          # or 1 の場合は強制的に1に変換する
    if t == 3 and b == 1: # xor 1
        if op == 0:       # or 1の場合は
            return 1      # 元々が0 にする演算の場合は、1に変換する
        if op == 1:
            return 0      # 元々が1 にする演算の場合は、0に変換する
        if op == 2:
            return 3      # 元々がxor の場合は何もしない
        if op == 3:
            return 2      # 元々が何もしない場合は、xor演算を行う
    # 以下の場合はそのまま
    # and１の場合
    # or 0 の場合
    # xor 0 の場合
    return op

def ap(val, op):              # 演算する（合成関数）
    if op == 0:return 0       # x = 0  強制的に0に変換する
    if op == 1:return 1       # x = 1  強制的に1に変換する
    if op == 2:return val ^ 1 # xor 1  0->1, 1->0に変換する
    if op == 3:return val     # do nothing  何もしない

for _ in range(N):
    T, A = map(int, input().split())
    # 各bit毎にoperationを計算する
    for i in range(30):
        # i桁目のオペレーションを求める
        op[i] = op_to_new_op(op[i], T, (A >> i) % 2)
        # X[i] に対するオペレーションを実施する
        X[i] = ap(X[i], op[i])

    tmp = 0
    for i in range(30):
        tmp += X[i] << i

    print(tmp)

        

