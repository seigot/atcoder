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
N,M=map(int, input().split())

mat = [[-1]*N for _ in range(N)]
#print(mat)

# 移動できるマスの大きさを求める
pair = []
for x1 in range(10**3+1):
    for x2 in range(10**3+1):
        val = x1*x1 + x2*x2
        if val == M:
            pair.append((x1,x2))

            pair.append((x1*(-1) ,x2)     )
            pair.append((x1      ,x2*(-1)))
            pair.append((x1*(-1) ,x2*(-1)))
pair_set = set(pair)
pair = list(pair_set)
#print(pair)

# 幅優先探索
def bfs(t):

    x, y = t
    mat[x][y] = 0
    dq = deque()
    dq.append((x,y,0))

    while len(dq) != 0:
        tx, ty, td = dq.popleft()
        #print(tx, ty, td )
        for ii in range(len(pair)):
            dx = tx + pair[ii][0]
            dy = ty + pair[ii][1]
            #print(dx, dy)
            if 0 <= dx < N and 0 <= dy < N:
                if mat[dx][dy] == -1:
                    # 次の探索箇所候補
                    dq.append((dx,dy,td+1))
                    mat[dx][dy] = td+1
bfs((0, 0))
#print("---")
# ans
for ii in range(N):
    print(*mat[ii])