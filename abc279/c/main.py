# -*- coding: utf-8 -*-
# ACx70, TLEx4

import sys
import math

sys.setrecursionlimit(1000000)

DEBUG=False
# DEBUG=True

input = sys.stdin.readline

def dprintn(str,val):
    if DEBUG : print(str,'=',val, end=" , ")

def dprint(str,val):
    if DEBUG : print(str,'=',val)

def printYes():
    print('Yes')

def printNo():
    print('No')

# リスト型標準入力
def input_list():
    dat = list(map(int,input().split()))
    return(dat)

# 2次元リスト型標準入力
def input_list_2d(lines):
    dat=[]
    for yy in range(lines):
        values = list(map(int,input().split()))
        # if len(values)==x:
        dat.append(values)
    return(dat)

inp = input_list()
H = inp[0]
W = inp[1]
dprintn('H',H)
dprint('W',W)

# 行列を入れ替える
#s=[]
s=[[] for ii in range(W)]
for ii in range(H):
    inp = input()
    for jj in range(W):
        if ii == 0:
#            s.append(str(inp[jj]))
            s[jj].append(inp[jj])
        else:
#            s[jj] = str(s[jj]) + str(inp[jj])
            s[jj].append(inp[jj])

#t=[]
t=[[] for ii in range(W)]
for ii in range(H):
    inp = input()
    for jj in range(W):
        if ii == 0:
#            t.append(str(inp[jj]))
            t[jj].append(inp[jj])
        else:
#            t[jj] = str(t[jj]) + str(inp[jj])
            t[jj].append(inp[jj])
s.sort()
t.sort()
dprint('s',s)
dprint('t',t)
for ii in range(W):
    if s[ii] != t[ii]:
        printNo()
        exit()
printYes()
exit()
