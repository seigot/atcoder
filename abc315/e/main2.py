#!/usr/bin/env python3                                                                          
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(4100000)
import math
import os
from inspect import currentframe
ONLINE_JUDGE = os.environ["HOME"] != "/Users/seigo"
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

N=int(input())
CP=[-1] + [list(map(int, input().split())) for h in range(N)]
error(CP)
gh = [[] for _ in range(N+2)] 
cntd = defaultdict(int)

need = set()
need.add(1)
for ii in range(1,N+1):
    if CP[ii][0] != 0:
        l = CP[ii][1:]
        for v in l:
            gh[ii+1].append(v)
            cntd[v] += 1
            need.add(v)

error(gh)
error(cntd)
error(need)

cntd = [0]*(N+1)
for i in need:
    for nxt in CP[i][1:]:    
        cntd[nxt] += 1

def bfs(s):
    que = deque()
    que.append(s)
    ans = []
    while que:
        crr = que.popleft()
        ans.append(crr)
        for nxt in CP[crr][1:]:
            cntd[nxt] -= 1
            if cntd[nxt] == 0:
                que.append(nxt)
    return ans

ans = bfs(1)
error(ans)
print(*ans[1:][::-1])
