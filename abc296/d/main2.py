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
from itertools import permutations,combinations
from copy import deepcopy
dpos2 = ((1, 0), (0, 1))
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

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

N,M=map(int, input().split())

ans = -1
for val in range(M,N**2+1):
    A = prime_factorization(val)
    # 素数をlist形式で出力 ex. [2, 2, 2, 3, 4]
    if len(A) == 1:
        a = 1
        b = val
        if b <= N:
            print(val)
            exit(0)
    else:
        # len(A) >= 2
        AA = deque(A)
        a = AA.popleft()
        b = AA.popleft()
        while AA:
            v = AA.popleft()
            if a < b:
                a *= v
            else:
                b *= v
        if a <= N and b <= N:
            print(val)
            exit(0)
print(ans)

