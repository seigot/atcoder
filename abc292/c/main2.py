#!/usr/bin/env python3                                                                          
import sys
input = sys.stdin.readline
sys.setrecursionlimit(4100000)
import math
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush
from math import gcd
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
MOD = 998244353
INF = float("inf")
MINF = -float("inf")
from itertools import permutations, combinations


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

N=int(input())                     # (1)数字が1つ 入力例:N

# AB*CD = N
# X * Y = N と考える、X,Yの組み合わせはN通り
# X=AB,Y=CDと表すことが何通りできるかどうかをそれぞれ考える

ans = 0
for X in range(1,N):
    Y = N - X
#    print("---",X,Y)
    # X=AB,Y=CDと表すことが何通りできるかどうかをそれぞれ考える
    # X=AB
    l = prime_factorization(X)
    l.append(1)
    #print(l)
    num_kind = set()
    # 1~len(l)個の組み合わせを網羅する
    for ii in range(1,len(l)+1):
        # ii個選択する場合
        for jj in permutations(range(len(l)), ii):
            val = 1
#            print("ii",ii,"jj",jj)
            for kk in range(ii):
                val *= l[jj[kk]]
            num_kind.add(val)
#        print(len(num_kind))
    ans1 = len(num_kind)

    # Y=CD
    l = prime_factorization(Y)
    l.append(1)
#    print(l)
    num_kind = set()
    # 1~len(l)個の組み合わせを網羅する
    for ii in range(1,len(l)+1):
        # ii個選択する場合
        for jj in permutations(range(len(l)), ii):
            val = 1
            for kk in range(ii):
                val *= l[jj[kk]]
            num_kind.add(val)
    ans2 = len(num_kind)

    ans += ans1 * ans2
print(ans)
