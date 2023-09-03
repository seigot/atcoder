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

Ha,Wa=map(int, input().split())
HWa = [list(input()) for h in range(Ha)]
Hb,Wb=map(int, input().split())
HWb = [list(input()) for h in range(Hb)]
Hx,Wx=map(int, input().split())
HWx = [list(input()) for h in range(Hx)]
error(HWa)
error(HWb)
error(HWx)

def checkalldot(_hw,offset2):
    cnt = 0
    for jj in range(30):
       for ii in range(30):
           if _hw[jj][ii] == ".":
               cnt += 1
    if cnt != 900 - offset2:
        return False
    return True

def check(hw):
    for jj in range(30-Hx):
       for ii in range(30-Wx):
            flag = True
            offset2 = 0
            for jjj in range(Hx):
                for iii in range(Wx):
                    if hw[jj+jjj][ii+iii] != HWx[jjj][iii]:
                        flag = False
            for jjj in range(Hx):
                for iii in range(Wx):
                    if hw[jj+jjj][ii+iii] == HWx[jjj][iii] == "#":
                        offset2 += 1
            if flag == True and checkalldot(hw,offset2) == True:
                return True
    return False


# 30*30のマスに合わせる
# 1.Aを(10,10)に置く
# 2.Bを0,0から(20,20)まで置いていく
# 3.一致するかどうか全探索check

def getHWtmp():
    HWtmp = [list("..............................") for h in range(30)]
    offset = 10
    for jj in range(Ha):
        for ii in range(Wa):
            HWtmp[jj+offset][ii+offset] = HWa[jj][ii]
    return HWtmp

for _jj in range(30-Hb):
    for _ii in range(30-Wb):
        _HWtmp = getHWtmp()
        # 2.
        for _jjj in range(Hb):
            for _iii in range(Wb):
                if HWb[_jjj][_iii] == ".":
                    continue
                _HWtmp[_jj+_jjj][_ii+_iii] = HWb[_jjj][_iii]
#        error(_HWtmp)
        if check(_HWtmp) == True:
            print("Yes")
            exit()
print("No")
