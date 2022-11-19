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
p = [] #[] for ii in range(4)]
for ii in range(4):
    x, y = map(int, input().split())
    p.append((x,y))

# 外積が負かどうかのチェック
def check_vec(p0, p1, p2):
    x0 = p0[0]
    y0 = p0[1]
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]

    # vector
    vec1_x = x1 - x0
    vec1_y = y1 - y0
    vec2_x = x1 - x2
    vec2_y = y1 - y2

    # sin(theta)
    ddd = (((vec1_x**2+vec1_y**2)**0.5)*((vec2_x**2+vec2_y**2)**0.5))
    val = (vec1_x*vec2_y - vec2_x*vec1_y)/ddd

    #print(x1,y1,x2,y2)
    #print(val)
    if val < 0:
        # 座標系が逆なので角度の正負も逆
        return True
    else:
        return False


# 外積を求める
ans = "Yes"
for ii in range(4):
    p0 = p[(ii-1)%4]
    p1 = p[ii%4]
    p2 = p[(ii+1)%4]
    if check_vec(p0, p1, p2) != True:
        ans = "No"
print(ans)
