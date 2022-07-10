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
for ii in range(N):
    s = S[ii]
    w = W[ii]
    l.append([w, s])
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
cnt = S_sort[0:N+1].count("1")
ans = max(ans, cnt)
prev = l[0][0]
for ii in range(0, N):
    cnt = 0
    # 着目している部分の値が0か1かによってcntを更新する
    cnt += S_sort[0:ii+1].count("0")
    cnt += S_sort[ii+1:N+1].count("1")
    #print(cnt)
    # 区切ることが可能でない場合はスキップ
    if ii != N-1:
        if l[ii][0] == l[ii+1][0]:
            continue
    ans = max(ans, cnt)
# 終端の区切り
cnt = 0
cnt += S_sort[0:N+1].count("0")
ans = max(ans, cnt)

print(ans)
