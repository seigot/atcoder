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

H,W,N,h,w=map(int, input().split())
A = [list(map(int, input().split())) for h in range(H)] # maze(1 2 3 4) のようなスペースありの2次元配列で受け取り
#print(maze)

kind = defaultdict(int)
# 種類の初期値を求める
for jj in range(H):
    for ii in range(W):
        kind[A[jj][ii]] += 1

import copy
# 窓をスライドして種類の値を変えていく
ans = [] 
for jj in range(H-h+1):
    ans_t = []
    tkind = copy.deepcopy(kind)
    for ii in range(W-w+1):
        # 窓の部分を消す
        if ii == 0:
            # ii==0の場合は素直に消す
            for ll in range(h):
                for kk in range(w):
                    val = A[ll+jj][kk+ii]
                    tkind[val] -= 1
                    if tkind[val] == 0:
                        del tkind[val]
        else:
            # ii>=1の場合は差分に着目
            # 追加
            for ll in range(h):
                val = A[ll+jj][ii-1]
                tkind[val] += 1
            # 削除
            for ll in range(h):
                val = A[ll+jj][ii+w-1]
                tkind[val] -= 1
                if tkind[val] == 0:
                    del tkind[val]
#        print(tkind.keys())
#        print(len(tkind.keys()))
#        print(tkind)
        ans_t.append(len(tkind.keys()))
    ans.append(ans_t)
for ii in range(len(ans)):
    print(*ans[ii])
