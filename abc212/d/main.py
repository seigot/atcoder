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

# https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py
import math
from bisect import bisect_left, bisect_right
from typing import Generic, Iterable, Iterator, TypeVar, Optional, List
T = TypeVar('T')

class DeletablePQ:
  def __init__(self,data=None,greater=False):
    self.greater=greater
    self.count= {}
    self.que=[]
    if data:
        for x in data:
            heappush(self.que,x*(-1 if greater else 1))
            if self.count.get(x): self.count[x] += 1
            else: self.count[x] = 1
    self.len = len(self.que)

  def push(self,x):
    heappush(self.que,x*(-1 if self.greater else 1))
    if self.count.get(x): self.count[x] += 1
    else: self.count[x] = 1
    self.len += 1
    
  def remove(self,x):
    self.count[x] -= 1
    self.len -= 1
  
  def nremove(self,x,num=1):
    self.count[x] -= num
    self.len -= num
    if self.count[x] < 0:
      self.len -= self.count[x]
      self.count[x] = 0
    
  def pop(self):
    x,self.count[x]=-1,0
    while self.count[x]<1: x=heappop(self.que)*(-1 if self.greater else 1)
    self.len -= 1
    self.count[x] -= 1
    return x
  
  def count(self,x):
    return self.count[x] if self.count[x]>0 else 0
  
  def get_val(self):
    while self.count.get(self.que[0]*(-1 if self.greater else 1)) != None and self.count[self.que[0]*(-1 if self.greater else 1)]<1:
        heappop(self.que)
    return self.que[0]*(-1 if self.greater else 1)

  def merge(self, other):
        while len(other) > 0: self.push(other.pop())
  
  def __len__(self):
    return self.len

Q=int(input())
query=[list(map(int, input().split())) for q in range(Q)]

called = DeletablePQ()
#called = []
sumdiff = 0
for ii in range(Q):
    q = query[ii]
    error(called,sumdiff)
    error(q)
    if q[0] == 1:
        x = q[1]
        called.push(x-sumdiff)     # 追加
#        heappush(called, x-sumdiff)
    if q[0] == 2:
        x = q[1]
        sumdiff += x
    if q[0] == 3:
#        x = called.pop()
        x = called.get_val()
        called.remove(x)
#        called.discard(x)   # 削除
#        x = heappop(called)
        print(x+sumdiff)
