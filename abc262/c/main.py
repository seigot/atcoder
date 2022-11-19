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
A = list(map(int, input().split()))
#print(A)
# 1≤i<j≤N
# min(ai,aj)=i
# max(ai,aj)=j
#  1) ai = i, aj = j
#  2) ai = j, aj = i

Ai_eq_i_cnt = 0
Ai_eq_j_cnt = 0
for i in range(len(A)):
    # 1)
    if A[i] == i+1:
        Ai_eq_i_cnt += 1
        continue
    # 2)
    if A[(A[i]-1)] == i+1:
        Ai_eq_j_cnt += 1

#print(Ai_eq_i_cnt, Ai_eq_j_cnt)
sum = (Ai_eq_i_cnt*(Ai_eq_i_cnt-1))//2
sum2 = Ai_eq_j_cnt//2
print(sum + sum2)