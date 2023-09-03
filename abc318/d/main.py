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

from itertools import combinations, permutations
import sys

N = int(input())
D = [[0 for j in range(N)] for i in range(N)]
for i in range(N - 1):
    d = list(map(int, input().split()))
    for j in range(i + 1, N):
        D[i][j] = D[j][i] = d[j - i - 1]

# usedフラグ(True:使用した, False:使用していない)を渡すDFS
# used = [False] * N
def dfs(used):
    if all(used):
        return 0
    # Falseのものから1つ選択する
    v = used.index(False)
    used[v] = True
    ret = 0
#    for w in range(v + 1, N):
    for w in range(N):
        # Falseの残り１つのものからもう1つ選択する
        if not used[w]:
            used[w] = True
            val = D[v][w] + dfs(used)
            ret = max(ret, val)
            used[w] = False
    used[v] = False
    return ret


used = [False] * N
ans = 0
if N % 2 == 0:
    ans = dfs(used)
else:
    for v in range(N):
        used[v] = True
        ans = max(ans, dfs(used))
        used[v] = False
print(ans)




