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

H, W, N=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
# indexあわせる
sx -= 1
sy -= 1
gx -= 1
gy -= 1

# 上下左右方向の障害物の位置をリストでもつ
xlist = defaultdict(list)
ylist = defaultdict(list)
for ii in range(N):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    xlist[x].append(y)
    ylist[y].append(x)
for ii in xlist.keys():
    xlist[ii].sort()
for ii in ylist.keys():
    ylist[ii].sort()
#print(xlist)
#print(ylist)

# cost
dist = defaultdict(lambda: INF)
#print(dist[(1,1)])

# 探索
#   y -->
# x
# |   (x,y)
# v
dq = deque()
# init
dq.append((sx, sy))
dist[(sx, sy)] = 0
while dq:
    tx, ty = dq.popleft()
    d = dist[(tx, ty)]
    #tx = tt[0]
    #ty = tt[1]
    #print("---")
    #print(tx, ty)
    #print("-")
    if tx == gx and ty == gy:
        break

    # 上(yが同じでx軸のマイナス)
    idx = bisect_left(ylist[ty], tx)
    if idx != 0:
        nx = ylist[ty][idx-1] + 1
        ny = ty
        #print("upper")
        #print(nx, ny)
        if dist[(nx, ny)] == INF:
            # 未探索
            dist[(nx, ny)] = d + 1
            dq.append((nx, ny))

    # 下(yが同じでx軸のプラス)
    idx = bisect_left(ylist[ty], tx)
    #print(idx)
    if idx != len(ylist[ty]):
        nx = ylist[ty][idx] - 1
        ny = ty
        #print("lowwer")
        #print(nx, ny)
        if dist[(nx, ny)] == INF:
            # 未探索
            dist[(nx, ny)] = d + 1
            dq.append((nx, ny))

    # 左(y軸のマイナス)
    idx = bisect_left(xlist[tx], ty)
    if idx != 0:
        nx = tx
        ny = xlist[tx][idx-1] + 1
        #print("left")
        #print(nx, ny)
        if dist[(nx, ny)] == INF:
            # 未探索
            dist[(nx, ny)] = d + 1
            dq.append((nx, ny))

    # 右(y軸のプラス)
    idx = bisect_left(xlist[tx], ty)
    if idx != len(xlist[tx]):
        nx = tx
        ny = xlist[tx][idx] - 1
        #print("right")
        #print(nx, ny)
        if dist[(nx, ny)] == INF:
            # 未探索
            dist[(nx, ny)] = d + 1
            dq.append((nx, ny))




ans = dist[(gx,gy)]
if ans == INF:
    print(-1)
else:
    print(ans)
