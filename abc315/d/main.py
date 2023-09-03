#!/usr/bin/env python3                                                                          
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(4100000)
import math
import os
from inspect import currentframe
ONLINE_JUDGE = os.environ["HOME"] == "/home/contestant"
def error1(*args, end="\n"): # 変数のみ表示
    if ONLINE_JUDGE: return
    print("[stderr]", *args, end=end, file=sys.stderr)
def error(*args): # 変数の名前と値をまとめて表示
    if ONLINE_JUDGE: return
    names = {id(v): k for k, v in currentframe().f_back.f_locals.items()}
    print("[stderr]",' '.join([names.get(id(arg), '???') + ' = ' + repr(arg) for arg in args]), file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from math import gcd
from itertools import permutations,combinations
from copy import deepcopy
dpos2 = ((1, 0), (0, 1))
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos4cross = ((1, 1), (1, -1), (-1, 1), (-1, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
MOD = 998244353
def invmod(a):
    return pow(a,-1,MOD)
INF = float("inf")
MINF = -float("inf")
#https://atcoder.jp/contests/ABC315/tasks/ABC315_d 
import sys
sys.setrecursionlimit(5*10**5)
input = sys.stdin.readline
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush
from bisect import bisect_left, bisect_right
from math import gcd


h,w = map(int,input().split())
col = [list(input().rstrip()) for i in range(h)]

r = [[0]*26 for i in range(h)] # 行方向
c = [[0]*26 for i in range(w)] # 列方向

# 縦横方向の各文字の出現数をカウントしておく
# 該当行/列が削除されたかどうかを管理しておく
# 削除候補/実際に削除された行/列を明示的に管理し分けられるようにする

# 縦横方向の各文字の出現数をカウント
for i in range(h):
    for j in range(w):
        col[i][j] = ord(col[i][j]) - ord("a")
        r[i][col[i][j]] += 1 # 出現回数+1
        c[j][col[i][j]] += 1 # 出現回数+1

R = set()
C = set()
while True:
    rr = set()
    cnt = [0]*26
    # 1. 行方向に着目する
    for i in range(h):
        if i in R: continue # 該当行が操作済みの場合?スキップ
        for j in range(26): # 各文字に着目
            if r[i][j] == w-len(C) and r[i][j] >= 2: # 全て同じ色、かつ、出現個数が2個以上
                rr.add(i)      # 削除候補行に追加
                cnt[j] += 1    # 削除候補個数に追加

    # 2. 列方向に着目する
    cc = set()
    cnt2 = [0]*26
    for i in range(w):
        if i in C: continue # 該当列が操作済みの場合?スキップ
        for x in range(26): # 各文字に着目
            if c[i][x] == h-len(R) and c[i][x] >= 2: # 全て同じ色、かつ、出現個数が2個以上
                cc.add(i)      # 削除候補行に追加
                cnt2[x] += 1   # 削除候補個数に追加 # 削除対象業の文字の出現個数

    # 3.削除
    ## 横の列
    for i in range(h):
        if i in R: continue
        if i in rr:   # 削除対象行の場合
            r[i] = [0] #[0] # 個数をゼロにする
            # # 削除済み扱いの行にする
            R.add(i)
            continue
        for j in range(26):
            # 該当行に残っている文字の数を求める
            # 列方向の各文字の出現回数の差をとる
            r[i][j] -= cnt2[j]
    ## 縦の列
    for i in range(w):
        if i in C: continue
        if i in cc:   # 削除対象列の場合
            c[i] = [0] # [0] # 個数をゼロにする
            # # 削除済み扱いの列にする
            C.add(i)
            continue
        for j in range(26):
            # 該当行に残っている文字の数を求める
            # 行方向の各文字の出現回数の差をとる
            c[i][j] -= cnt[j]

    # exit()
    # どの行も削除ができない場合は探索終了
    if len(rr) == 0 and len(cc) == 0:
        break

print(sum([sum(i) for i in r]))
    
