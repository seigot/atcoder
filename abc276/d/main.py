#!/usr/bin/env python3
import sys
sys.setrecursionlimit(4100000)
import math
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

# A,B=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
N = int(input())
A = list(map(int, input().split()))

# 1.最大公約数を求める
#     最大公約数でAの各値を割る
#     割り切れない場合は-1
# 2.素因数分解する(2,3)
#     それぞれの回数を足した数が答え

# 1.
#Agcd = min(A)
Agcd = A[0]
for ii in range(1, len(A)):
    Agcd = math.gcd(Agcd, A[ii])
#print(Agcd)

for ii in range(len(A)):
    val = A[ii]//Agcd
    mod = A[ii]%Agcd
    A[ii] = val

# 2.
ans = 0
for ii in range(len(A)):
    val = A[ii]
    # 2で割る
    while val%2 == 0:
        val = val/2
        ans += 1
    # 3で割る
    while val%3 == 0:
        val = val/3
        ans += 1
#    print(val)
    if val != 1:
        print(-1)
        exit(0)
print(ans)
