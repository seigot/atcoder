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

N=int(input())

def primes(x):
    # 0以上整数x「未満」の素数をリストに格納して返す
    # https://nekotheshadow.github.io/qiita-backup/blog/4ebad619564a48f5a97f/
    if x < 2: return []

    primes = [i for i in range(x)]
    primes[1] = 0 # 1は素数ではない

    # エラトステネスのふるい
    for prime in primes:
        if prime > math.sqrt(x): break
        if prime == 0: continue
        for non_prime in range(2 * prime, x, prime): primes[non_prime] = 0
    return [prime for prime in primes if prime != 0]

def sieve(L,R):
    if L<2: L=2
    flag=[0]*(R+1)
    for i in range(2, min(R+1,int(R**.5)+5)):
        if flag[i]:continue
        for j in range(i**2,R+1, i):
            if flag[j]:continue
            if j % i == 0: flag[j] = 1
    # return [i for i in range(L,R+1) if flag[i] == 0], flag #flagをèしたæがäåなåå
    return [i for i in range(L,R+1) if flag[i] == 0]
  
# Nまでの素数リストを取得
#l = primes(10**6+100)
l = sieve(0,10**6+100) 

ans = []
for ii in range(len(l)):
    p = l[ii]
    for jj in range(ii+1, len(l)):
        q = l[jj]
        k = p*q**3
        if k > N:
            break
        error(k)
        ans.append(k)
error(ans)
print(len(ans))
