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

class SCC:
    '''
    SCC class with non-recursive DFS.
    '''
    def __init__(self,N):
        self.N = N
        self.G1 = [[] for _ in range(N)]
        self.G2 = [[] for _ in range(N)]
        self.g = None
        
    def add_edge(self,a,b):
        self.G1[a].append(b)
        self.G2[b].append(a)
    
    def scc(self):
        self.seen = [0]*self.N
        self.postorder=[-1]*self.N
        self.order = 0
        for i in range(self.N):
            if self.seen[i]:continue
            self._dfs(i)
        
        self.seen = [0]*self.N
        self.scclist = []
        for i in self._argsort(self.postorder,reverse=True):
            if self.seen[i]:continue
            cc = self._dfs2(i)
            self.scclist.append(cc)
            
        return self.scclist

    def group(self):
        self.g = [0]*self.N
        for i,cc in enumerate(self.scclist):
            for v in cc: self.g[v] = i
        return self.g

    def small_graphs(self):
        if not self.g: self.g = self.group()
        self.Glist = [[[] for _ in range(self.N)] for _ in range(len(self.scclist))]
        for a in range(self.N):
            for b in self.G1[a]:
                if self.g[a] != self.g[b]: continue
                g = self.g[a]
                self.Glist[g][a].append(b)
        return self.Glist
      
    def dag(self):
      if not self.g: self.g = self.group()
      self._dag = [set() for _ in range(len(self.scclist))]
      for i in range(self.N):
        for j in self.G1[i]:
          if self.g[i]==self.g[j]:continue
          gi,gj = self.g[i],self.g[j]
          self._dag[gi].add(gj)
      return self._dag
                
    def _argsort(self,arr,reverse=False):
        shift = self.N.bit_length()+2
        tmp = sorted([arr[i]<<shift | i for i in range(len(arr))],reverse=reverse)
        mask = (1<<shift) - 1
        return [tmp[i] & mask for i in range(len(arr))]
    
    def _dfs(self,v0):
        todo = [~v0, v0]
        while todo:
            v = todo.pop()
            if v >= 0:
                self.seen[v] = 1
                for next_v in self.G1[v]:
                    if self.seen[next_v]: continue
                    todo.append(~next_v)
                    todo.append(next_v)
            else:
                if self.postorder[~v] == -1:
                    self.postorder[~v] = self.order
                    self.order += 1
    
    def _dfs2(self,v):
        todo = [v]
        self.seen[v] = 1
        cc = [v]
        while todo:
            v = todo.pop()
            for next_v in self.G2[v]:
                if self.seen[next_v]: continue
                self.seen[next_v] = 1
                todo.append(next_v)
                cc.append(next_v)
        return cc
      
N=int(input())
s2i = {}
scc = SCC(2*N)
for _ in range(N):
  S,T = input().split()
  # 強連結成分分解するために、登場番号順に変換
  if S not in s2i:
    s2i[S] = len(s2i)
  if T not in s2i:
    s2i[T] = len(s2i)   
  scc.add_edge(s2i[S],s2i[T])
#  scc.add_edge(int(S),int(T))
  
scclist = scc.scc()
error(scclist)
for g in scclist:
  if len(g) > 1:
    print("No")
    exit()
print("Yes")