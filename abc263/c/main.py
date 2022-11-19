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
# 長さ N かつ全ての要素が 1 以上 M 以下である整数列のうち、狭義単調増加であるものを全て辞書順に出力してください。
N, M = map(int, input().split())

# 全探索
# bitが立っているところに値を入れることを繰り返す
ans = []
for bit in range(1<<M): # Max10桁
    #print(bit)
    A = []
    # M以下の整数
    # bitが立っているところに値を入れる
    # 0 0 1 1 1 となっていたら 3,4,5 を入れる
    # 1 1 1 0 0 となっていたら 1,2,3 を入れる
    for i in range(M):
        if bit & 1:
            # bitが立っている
            A.append(i+1)
        bit >>= 1
    #print(A)
    # 長さがNのもの
    if len(A) == N:
        #print(A)
        ans.append(A)
ans.sort()

for a in ans:
    print(*a)
