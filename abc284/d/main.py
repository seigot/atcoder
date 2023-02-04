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

T=int(input())
test = []
for ii in range(T):
    t=int(input())
    test.append(t)
#print(test)

# 素因数分解
# 素因数 p と 指数 e の組を格納
def fact(n):
  l = []
  tmp = n
  # sqrt(N)より大きい素因数は高々1つしか出ないので探索範囲を限定する
  for i in range(2,int(pow(n,1))+1):
    if tmp % i == 0:
      cnt = 0
      while tmp % i == 0:
        cnt += 1
        tmp //= i
      l.append([cnt,i])

      # p**2 * qの制約より、もう一つを特定する
      ii = n//(pow(i,cnt))
      cntii = 3-cnt
      if cntii == 2:
        #ii = int(math.sqrt(ii))
        #ii = int(ii**(1/cntii))
        l.append([cntii,int(ii**(1/cntii))])
      else:
        l.append([cntii,ii])
      
      return l

# 探索
for ii in range(T):
    val = test[ii]
    l = fact(val)
    l.sort()
    print(l[1][1], l[0][1])
