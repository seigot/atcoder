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

# A,B=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
H,W=map(int, input().split())
C = [] * H
Si = None
for jj in range(H):
    c = input()
    C.append(c)
    if 'S' in c:
        ii = c.index('S')
        Si = (ii,jj)
#        C[ii][jj] = "#"
#print(Si)
#print(C)
#print(C[Si[1]][Si[0]])

# 深さ優先探索
def bfs(ix, iy):

    # init
    if ix < 0 or W <= ix or iy < 0 or H <= iy:
        return 0
    if C[iy][ix] == "#":
        return 0

    dq = deque()
    dq.append((ix,iy,0))
    s = set()
    s.add((ix,iy))

    # 幅優先探索
    while dq:
        tx, ty, td = dq.popleft()
#        print(tx, ty, td, C[ty][tx])
        # 探索
        for dd in dpos4:
            dx = tx + dd[0]
            dy = ty + dd[1]
            dd = td + 1

            # 領域外ではない
            if dx < 0 or W <= dx or dy < 0 or H <= dy:
                continue
            # goal
            if dd >= 3 and C[dy][dx] == "S":
#                print(tx, ty, td, C[ty][tx])
                print("Yes")
                exit(0)
            # 壁や領域外ではない
            if C[dy][dx] != "#" and C[dy][dx] != "S":
                # 未探索
                if (dx,dy) not in s:
                    # 探索候補
                    dq.append((dx,dy,dd))
                    s.add((dx,dy))

bfs(Si[0]+1, Si[1])
bfs(Si[0]  , Si[1]+1)
bfs(Si[0]-1, Si[1])
bfs(Si[0]  , Si[1]-1)
print("No")
