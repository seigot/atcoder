#!/usr/bin/env python3                                                                          
import sys
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

N,K = map(int,input().split())
# 1~Kまで全部繋げた場合の偶奇を尋ねる
query = list(range(1,K+1))
print(" ".join(["?"]+list(map(str,query))),flush=True)
par0 = int(input())

data = [0]*N
#data[K-1] = par0
# K+1~Nまでの偶奇チェック
for i in range(N-K):
  query[-1] += 1
  print(" ".join(["?"]+list(map(str,query))),flush=True)
  par = int(input())
  if par != par0:
    # 1~Kの偶奇と異なる場合は1にする
    data[i+K] = 1

query[-1] = K+1 # queryの最後をK+1(Kの1つ後ろ)に戻す
# 1~K-1までの偶奇チェック
for i in range(K-1): # K-1個ぶんチェックする
  query[i] = K    # index=iの部分を更新する
  print(" ".join(["?"]+list(map(str,query))),flush=True)
  query[i] = i+1  # 更新した部分を元に戻す
  par = int(input())
#  if data[K-1] == data[K]:
    # K-1,Kの偶奇が一致する場合
    # もしpar == par0の場合
    #   該当の値 + data[K] == 偶数
    #   --> 該当の値と、data[K]の偶奇も一致 == 基準となるK-1との偶奇も一致
    #   なのでdata[i] == 0
    # もし par != par0の場合
    #   該当の値 + data[K] == 奇数
    #   --> 該当の値と、data[K]の偶奇は不一致 == 基準となるK-1との偶奇も不一致
    #
    # 対象の値(i)とKが同じ場合は基準の偶奇と一致するはずであるが、異なる場合は異なる値にする
  if (par + par0)%2 == 0:
    data[i] = data[K]
  else:
    data[i] = data[K]^1

if sum(data[:K])%2 != par0:
  # 基準となる偶奇（1~K）までの偶奇が異なる場合は、
  # 解答を反転する
  data = [d^1 for d in data]
      
print(" ".join(["!"]+list(map(str,data))),flush=True)
exit()