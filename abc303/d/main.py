#!/usr/bin/env python3                                                                          
import sys
#input = sys.stdin.readline # 文字列Sの場合は最後に"¥n"が付くので注意
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

x,y,z=map(int, input().split())
s=input()
# dp[i][j] 「 i 文字目まで入力した時点で CapsLock キーのランプが j=0 ならばOFF、j=1 ならばONである状態にするために必要な時間の最小値」
dp = [[INF]*(2) for _ in range(len(s)+1)]
dp[0][0] = 0
dp[0][1] = z

for i in range(1, len(s)+1):
    # 貰うdp
    if s[i-1] == "a": 
        # i文字目が小文字
        dp[i][0] = min(dp[i-1][0] + x,      # [CapsLockなし] + aキーのみ押す                         ---> [CapsLockなし]
#                      dp[i-1][0] + z+y+z,  # [CapsLockなし] + [shift+a] + CapsLock                ---> [CapsLockなし]
                       dp[i-1][1] + y + z,  # [CapsLockあり] + [shift+a] + CapsLock                ---> [CapsLockなし]
                       dp[i-1][1] + z + x)  # [CapsLockあり] + [CapsLock] + a                      ---> [CapsLockなし]
        dp[i][1] = min(dp[i-1][0] + x + z,  # [CapsLockなし] + a + CapsLock                        ---> [CapsLockあり]
                       dp[i-1][0] + z + y,  # [CapsLockなし] + CapsLock + [shift+a]                ---> [CapsLockあり]
                       dp[i-1][1] + y,         # [CapsLockあり] + [shift+a]                        ---> [CapsLockあり]
#                       dp[i-1][1] + z + x + z) # [CapsLockあり] + [CapsLock] + a + [CapsLock]      ---> [CapsLockあり]
        )
    else: 
        #i文字目が大文字
        dp[i][0] = min(dp[i-1][0] + y,      # [CapsLockなし] + [shift+a] + [CapsLock]      ---> [CapsLockなし]
                       dp[i-1][0] + z+x+z,  # [CapsLockなし] + [CapsLock] + A + [CapsLock] ---> [CapsLockなし]
                       dp[i-1][1] + x + z,  # [CapsLockあり] + A + [CapsLock]              ---> [CapsLockなし]
#                       dp[i-1][1] + z + y  # [CapsLockあり] + [CapsLock] + [shift+a]      ---> [CapsLockなし]
        )
        dp[i][1] = min(dp[i-1][0] + y+z,    # [CapsLockなし] + [shift+a] + [CapsLock]      ---> [CapsLockあり]
                       dp[i-1][0] + z+ x,   # [CapsLockなし] + [CapsLock] + A              ---> [CapsLockあり]
                       dp[i-1][1] + x,       # [CapsLockあり] + A                                        ---> [CapsLockあり]
#                       dp[i-1][1] + z + y+z) # [CapsLockあり] + [CapsLock] + [shift+a] + [CapsLock]      ---> [CapsLockあり]
        )
print(min(dp[-1]))