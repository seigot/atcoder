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

# HWxマスの"."を削除した矩形を返す
# ......
# ..##..
# ..##..
# ......
#
# ##
# ##
# _HW,y,x

def get_removedoxMatrix(_hw,_h,_w):
    minx = INF
    miny = INF
    maxx = -INF
    maxy = -INF
    for jj in range(_h):
        for ii in range(_w):
            if _hw[jj][ii] == "#":
                minx = min(ii,minx)
                miny = min(jj,miny)
                maxx = max(ii,maxx)
                maxy = max(jj,maxy)
    __hw = [[] for h in range(maxy-miny+1)]
    for jj in range(maxy-miny+1):
        __hw[jj] = _hw[miny+jj][minx:minx+(maxx-minx)+1]
    return __hw, maxy-miny+1, maxx-minx+1
_HWa, _Ha, _Wa = get_removedoxMatrix(HWa,Ha,Wa)
_HWb, _Hb, _Wb = get_removedoxMatrix(HWb,Hb,Wb)
_HWx, _Hx, _Wx = get_removedoxMatrix(HWx,Hx,Wx)

if _Hx < _Ha or _Hx < _Hb or _Wx < _Wa or _Wx < _Wb:
    # 範囲外
    print("No")
    exit()

for jja in range(_Hx-_Ha+1):
    for iia in range(_Wx-_Wa+1):
        for jjb in range(_Hx-_Hb+1):
            for iib in range(_Wx-_Wb+1):
                # (jja,iia),(jjb,iib)
                tmpHW = [ list("."*_Wx) for _ in range(_Hx)]
                # A
                for jjj in range(_Ha):
                    for iii in range(_Wa):
                        if _HWa[jjj][iii] == "#":
                            tmpHW[jja+jjj][iia+iii] = _HWa[jjj][iii]
                # B 
                for jjj in range(_Hb):
                    for iii in range(_Wb):
                        if _HWb[jjj][iii] == "#":
                            tmpHW[jjb+jjj][iib+iii] = _HWb[jjj][iii]
                if tmpHW == _HWx:
                    print("Yes")
                    exit()
print("No")