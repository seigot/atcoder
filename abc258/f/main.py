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

def bigShortest(Sx, Sy, Gx, Gy, B):
    # 大通りの距離を求める
    if Sx % B == 0 and Gx % B == 0 and Sy // B == Gy // B and not(Sx // B == Gx // B):
        # 迂回する場合(xが大通りに平行で、yが同じようなブロックにいるパターン)
        return min(
            Sy % B + Gy % B + abs(Gx - Sx),         # 降りて登るパターン
            B - Sy % B + B - Gy % B + abs(Gx - Sx)  # 上から行くパターン
        )
    if Sy % B == 0 and Gy % B == 0 and Sx // B == Gx // B and not(Sy // B == Gy // B):
        # 迂回する場合(yが大通りに平行で、xが同じようなブロックにいるパターン)
        return min(
            Sx % B + Gx % B + abs(Gy - Sy),         # 左回りで行くパターン
            B - Sx % B + B - Gx % B + abs(Gy - Sy)  # 右回りで行くパターン
        )
    # 迂回せず辿り着けるケース
    return abs(Sx - Gx) + abs(Sy - Gy)

def solve():
    B, K, Sx, Sy, Gx, Gy = map(int, input().split())
    # 一回も大通りを通らないケース
    ans = (abs(Sx - Gx) + abs(Sy - Gy)) * K
    # 大通りを通るケース
    for i in range(4):
        # 小通り（最初）
        distS = 0
        if i == 0:
            sx, sy = Sx // B * B, Sy       # 左端
            distS += Sx % B                # 距離
        if i == 1:
            sx, sy = Sx, Sy // B * B       # 下
            distS += Sy % B                # 距離
        if i == 2:
            sx, sy = Sx // B * B + B, Sy   # 右端
            distS += B - Sx % B            # 距離
        if i == 3:
            sx, sy = Sx, Sy // B * B + B   # 上
            distS += B - Sy % B            # 距離
        for j in range(4):
            # 小通り（最後）
            distG = 0
            if j == 0:
                gx, gy = Gx // B * B, Gy   # 左端
                distG += Gx % B            # 距離
            if j == 1:
                gx, gy = Gx, Gy // B * B   # 下
                distG += Gy % B            # 距離
            if j == 2:
                gx, gy = Gx // B * B + B, Gy  # 右端
                distG += B - Gx % B           # 距離
            if j == 3:
                gx, gy = Gx, Gy // B * B + B  # 上
                distG += B - Gy % B           # 距離
            ans = min(ans, distS * K + distG * K + bigShortest(sx, sy, gx, gy, B))
    print(ans)




T = int(input())

for _ in range(T):
    solve()

