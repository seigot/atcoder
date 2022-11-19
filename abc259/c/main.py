#!/usr/bin/env python3
from re import A
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
S=input()
T=input()

if S == T:
    print("Yes")
    exit(0)

S_array=[]
T_array=[]
# Sを圧縮
S_array_idx = 0
for i in range(len(S)):
    if i == 0:
        S_array.append([S[i],1])
        continue
    if S_array[S_array_idx][0] == S[i]:
        S_array[S_array_idx][1] += 1
    else:
        S_array.append([S[i],1])
        S_array_idx += 1
# Tを圧縮
T_array_idx = 0
for i in range(len(T)):
    if i == 0:
        T_array.append([T[i],1])
        continue
    if T_array[T_array_idx][0] == T[i]:
        T_array[T_array_idx][1] += 1
    else:
        T_array.append([T[i],1])
        T_array_idx += 1

# 比較する
if len(S_array) != len(T_array):
    print("No")
    exit(0)
for i in range(len(S_array)):
    # Sの文字列を追加する事に注意する
    #if S_array[i][1] >= 2:
    #    S_array[i][1] = 2
    #if T_array[i][1] >= 2:
    #    T_array[i][1] = 2
    if S_array[i][1] >= 2 and S_array[i][1] < T_array[i][1]:
        S_array[i][1] = T_array[i][1]

    if S_array[i][0] == T_array[i][0] and S_array[i][1] == T_array[i][1]:
        pass
    else:
        print("No")
        exit(0)
print("Yes")
