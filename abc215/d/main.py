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

N,M=map(int, input().split())
A=list(map(int, input().split()))

def prime_factorization(n):
    """
    task:prime factorization
    return:prime
    type:list
    """
    l=[]
    for i in range(2,int(n**0.5)+1): # 割り算のTryは2から、平方根以下まで
        while True:
            if n%i == 0:
                l.append(i) # 余り0なら素因数分解リストにappendする
                n = n//i # nの更新
            else:
                break
    if n > int(n**0.5): # nが　int(n**0.5) より大きなポイントでbreakしていたらそれをリストにappend 素数の時もこれ
        l.append(n)
    return l

# 約数の集合を求める
S = set()
error(S)
for a in A:
#    l = make_divisors(a)
    l = prime_factorization(a)
    error(l)
    s = set(l)
    error(s)
#    S = S.union(s)
    S.update(s)
#    S |= s

error(S)
# 約数を削除していく
ans = set([ii for ii in range(1,M+1)])
for s in S:
    error(ans)
#    if s > M:
#        continue
    if s == 1:
        continue
    else:
        for ii in range(s, M+1, s):
            if ii not in ans:
                continue
            error("discard",ii)
            ans.discard(ii)
print(len(ans))
print(*sorted(ans))
