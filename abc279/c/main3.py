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
        values = list(input())
        # if len(values)==x:
        dat.append(values)
    return(dat)

inp = input_list()
H = inp[0]
W = inp[1]
dprintn('H',H)
dprint('W',W)

# 行列を入れ替える

s=[]
inp2d = input_list_2d(H)
for jj in range(W):
    l = []
    for ii in range(H):
        l.append(inp2d[ii][jj])
    s.append(l)

t=[]
inp2d = input_list_2d(H)
for jj in range(W):
    l = []
    for ii in range(H):
        l.append(inp2d[ii][jj])
    t.append(l)

#s.sort()
#t.sort()
dprint('s',s)
dprint('t',t) 
if sorted(s) != sorted(t):
    printNo()
    exit()
#for ii in range(W):
#    if s[ii] != t[ii]:
#        printNo()
#        exit()
printYes()
exit()

