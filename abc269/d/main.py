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
gh = []
gh_s = set()

for ii in range(N):
    x, y = map(int, input().split())
    gh.append((x,y))
    gh_s.add((x,y))

# 探索済みかどうか
searched = set()

# 近傍
near = [(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1)]

# 探索
def search(x, y):

    dq = deque()
    dq.append((x,y))
    searched.add((x,y))

    # 幅優先探索
    while dq:
        x, y = dq.popleft()
        # 近傍探索
        for ii in range(len(near)):
            dx, dy = near[ii]
            tx = x + dx
            ty = y + dy
            # 黒色領域であり、かつ未探索の場合は次の探索候補にする
            if (tx,ty) not in searched:
                if (tx,ty) in gh:
                    dq.append((tx, ty))
                    searched.add((tx,ty))

# 各エリアを探索
ans = 0
for ii in range(N):

    x, y = gh[ii]
    if (x,y) not in searched:
        # 探索
        search(x, y)
        ans +=1

print(ans)