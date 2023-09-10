#!/usr/bin/env python3                                                                                                                                                                                                                              
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(4100000)
import math
import os
from inspect import currentframe
ONLINE_JUDGE = os.environ["HOME"] == "/home/runner"
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

C=[list(map(int, input().split())) for _ in range(3)]
error(C)


# 階乗計算
def factorial_recursive(num):
    if num == 0:
        return 1
    else:
        return num * factorial_recursive(num-1)
    
# check gakkari
def check_gakkari(crr,length,visited):
    mat = [[-1]*3 for _ in range(3)]
    for i in visited:
        ix = int(i)%3
        iy = int(i)//3
        mat[iy][ix] = C[iy][ix]
#    print(mat)
    # vertical
    for xx in range(3):
        prev = defaultdict(int)
        latest = -1
        for yy in range(3):
            val = mat[yy][xx]
            if val != -1:  
                prev[val] += 1
                latest = val
        if prev[latest] == 2 and sum(prev.values()) == 2:
            return True

    # horizontal
    for yy in range(3):
        prev = defaultdict(int)
        latest = -1
        for xx in range(3):
            val = mat[yy][xx]
            if val != -1:  
                prev[val] += 1
                latest = val
        if prev[latest] == 2 and sum(prev.values()) == 2:
            return True
    # cross
    prev = defaultdict(int)
    latest = -1
    for yy in range(3):
        val = mat[yy][yy]
        if val != -1:  
            prev[val] += 1
            latest = val
    if prev[latest] == 2 and sum(prev.values()) == 2:
        return True
    prev = defaultdict(int)
    latest = -1
    for yy in range(3):
        val = mat[2-yy][yy]
        if val != -1:  
            prev[val] += 1
            latest = val
    if prev[latest] == 2 and sum(prev.values()) == 2:
        return True

    return False

# 幅優先探索
def bfs(s):
    que = deque()
    visited = str(s)
    que.append((s,1,visited)) # index,length,visited
    ans_cnt = 0
    while que:
        crr,crr_length,crr_visited = que.popleft()

        if check_gakkari(crr,crr_length,crr_visited) == True:
            #ans_cnt += factorial_recursive(9-crr_length)
            ans_cnt += math.factorial(9-crr_length)
            continue
        if crr_length == 9:
            continue
        for nxt_s in range(9):
            if str(nxt_s) in crr_visited:
                # 探索済
                continue
            nxt_visited = crr_visited + str(nxt_s)
            nxt_length = crr_length + 1
            que.append((nxt_s,nxt_length,nxt_visited))
    return ans_cnt

cnt = 0
for ii in range(9):
    c = bfs(ii)
    cnt += c
ans = cnt/(9*8*7*6*5*4*3*2*1)
print(1-ans)