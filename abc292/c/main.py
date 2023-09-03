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

# https://atcoder.jp/contests/abc292/submissions/39415106


def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    # 掛けてnとなる(a,b)の組み合わせを数える
#    while i*i <= n:
#        # 割った余りが0の場合
#        if n % i == 0:
#            lower_divisors.append(i)
#            # 組み合わせが同じ場合は重複するので数えない(ex.(2,2))
#            if i != n//i:
#                # もう一方の値
#               upper_divisors.append(n//i)
#        i += 1
    for i in range(1, int(math.sqrt(n))+1):
        # 割った余りが0の場合
        if n % i == 0:
            lower_divisors.append(i)
            # 組み合わせが同じ場合は重複するので数えない(ex.(2,2))
            if i == n//i:
               pass
            else:
                # もう一方の値
                upper_divisors.append(n//i)
    return lower_divisors + upper_divisors

N=int(input())
ans = 0
# 全探索(1~N)
for i in range(1,N):
    j = N-i
    n1 = len(make_divisors(i))
    n2 = len(make_divisors(j))
    ans += n1 * n2
    
print(ans)