import sys
input = sys.stdin.readline # 文字列Sの場合は最後に"¥n"が付くので注意
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

#from bisect import bisect, bisect_left, bisect_right
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



# --- 1.
from bisect import bisect_left, bisect_right
s = list(input())
n = len(s) - 1
k = int(input())
l = []
now = 0
for i in range(n):
    if s[i] == "X":
        l.append(now)
    else:
        now+= 1
        l.append(now)
ans = 0
# 先に累積和("."の数)を求めてから尺取り法
# 現在注目している"."の数+K個(or K-1個)のindexを二分探索で求める
# (上記で求めたindex) - (現在のindex) がXの連続する数
for i in range(n):
    offset = 0
    if s[i] == ".":
        offset = -1
    target = bisect_right(l,l[i]+k+offset)
    ans = max(ans,target-i)
print(ans)

# --- 2.
S=input()
K=int(input())
lenS = len(S)-1
error(S)
error(lenS)
 
# 尺取り法
l = 0
r = 0
Xmax = 0
Dotcnt = 0
while l < lenS: # lを基準に全探索
    error(l,r,Xmax,Dotcnt)
    # rを前進
    while Dotcnt <= K and r < lenS:
        if S[r] == ".":
            if Dotcnt == K:
                break
            Dotcnt += 1
        r += 1
        Xnum = r-l
        Xmax = max(Xmax, Xnum)
        error(l,r,Xmax,Xnum,Dotcnt)
        if Dotcnt <= K and r <= lenS:
            continue
        r -= 1
        break
 
    # lを前進
    if S[l] == ".":
        Dotcnt -= 1
    l += 1
print(Xmax)
#!/usr/bin/env python3                                                                          
import sys
input = sys.stdin.readline
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

S=input()
K=int(input())
lenS = len(S)-1
error(S)
error(lenS)

# 尺取り法
l = 0
r = 0
Xmax = 0
Dotcnt = 0
while l < lenS: # lを基準に全探索
    error(l,r,Xmax,Dotcnt)
    # rを前進
    while Dotcnt <= K and r < lenS:
        if S[r] == ".":
            if Dotcnt == K:
                break
            Dotcnt += 1
        r += 1
        Xnum = r-l
        Xmax = max(Xmax, Xnum)
        error(l,r,Xmax,Xnum,Dotcnt)
        if Dotcnt <= K and r <= lenS:
            continue
        r -= 1
        break

    # lを前進
    if S[l] == ".":
        Dotcnt -= 1
    l += 1
print(Xmax)
