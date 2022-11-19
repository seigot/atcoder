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
n,m = map(int,input().split())
a,b,c,d,e,f = map(int,input().split())
obj = set([tuple(map(int,input().split())) for i in range(m)])

# dp[n][x][y]=n回のワープ後に (x,y) にいるような移動経路の個数
# とするDPにより O(N3logM) 時間で問題を解くことができます

# メモ化でも解決可能
mem = [[[-1]*(n+1) for i in range(n+1)] for i in range(n+1)]

ans = [0]
def func(x,y,z):
    # x, y, z の選択肢をそれぞれ何回行ったのかを計算する
    nowx = a*x + c*y + e*z
    nowy = b*x + d*y + f*z
    if (nowx, nowy) in obj:
        # 対象が障害物の場合は探索できない旨を返す
        return 0
    if x + y + z == n:
        # ここの場合はこれ以上移動しないので1(通り)を返す
        return 1
    if mem[x][y][z] != -1:
        # 探索済みの場合はこれを返す
        # z --> z --> x のケース、 x --> z --> z のケース等の重複ケースがあり
        # かなりの効率化が期待できる
        return mem[x][y][z]
    # 次の座標
    tmp = 0
    tmp += func(x+1, y, z)
    tmp += func(x, y+1, z)
    tmp += func(x, y, z+1)
    tmp %= MOD
    mem[x][y][z] = tmp
    return tmp

val = func(0,0,0)
print(val)