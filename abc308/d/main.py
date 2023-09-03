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
from heapq import heappop, heappush
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

H,W=map(int, input().split())
maze = [list(input()) for h in range(H)]
snuke = "snuke"
#error(snuke)

# 深さ幅優先探索
# queueとvisitedのadd/discardを組み合わせて実装する
from collections import deque
visited = set()
visitedcommon = set()
def dfs(n):
    q = deque()
    q.appendleft(~n)
    q.appendleft(n)

    while q:
        # visitedへ追加
        error("---")
        tx = q.popleft()
        ii = (tx % (10**8)) % W
        jj = (tx % (10**8)) // W
        step = tx // (10**8)
        visited.add((ii,jj))
        error("tx", ii, jj, tx, q)
        visitedcommon.add((ii,jj))
        if tx >= 0:
            for (dx,dy) in dpos4:
                nx = ii + dx
                ny = jj + dy
                if nx < 0 or W <= nx or ny < 0 or H <= ny:
                    # out of range
                    error("out of range", nx, ny)
                    continue
                error(ny, nx, maze[ny][nx], snuke[(nx+ny)%5])
                if (nx,ny) in visitedcommon:
                    # already visited
                    error("already visited")
                    continue
                if maze[ny][nx] != snuke[(step+1)%5]:
                    # not goal
                    error("string differ", ny, nx, maze[ny][nx], snuke[(step+1)%5])
                    continue
                # not visited
                dd = nx + ny * W
                dd += (step+1)*(10**8)
                error("append", dd, ~dd, nx, ny, maze[ny][nx], snuke[(step+1)%5])
                q.appendleft(~dd)
                q.appendleft(dd)
#                visitedcommon.add((nx,ny))
                if (nx,ny) == (W-1,H-1):
                    print("Yes")
                    exit()
        else:
            # visitedから削除
            tx = ~tx
            ii = (tx % (10**8)) % W
            jj = (tx % (10**8)) // W
            visited.discard((ii,jj))
    return True
# 全頂点で探索
if maze[0][0] == "s":
    dfs(0)
print("No")
