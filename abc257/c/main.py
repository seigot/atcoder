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
S = input()
W = list(map(int,input().split()))

l = []
cnt = 0 # 1の数
for ii in range(N):
    s = S[ii]
    w = W[ii]
    l.append([w, s])
    if s == "1":
        cnt += 1
l.sort()

# bit列を数え直す
S_sort = ""
for ii in range(N):
    s = l[ii][1]
    S_sort = S_sort + s
#print(S_sort)

# ある時点を区切りとして、区切りの前の0と、区切りの後の1の数を数える
ans = 0
# 先端の区切り
ans = max(ans, cnt)
for ii in range(0, N):
    # 着目している部分の値が0か1かによってcntを更新する
    if S_sort[ii] == "0":
        cnt += 1
    elif S_sort[ii] == "1":
        cnt -= 1
    # 区切ることが可能でない場合はスキップ
    if ii != N-1:
        if l[ii][0] == l[ii+1][0]:
            continue
    ans = max(ans, cnt)
print(ans)
