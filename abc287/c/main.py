# -*- coding: utf-8 -*-
# ACx30 WAx6

import sys
import math

sys.setrecursionlimit(1000000)

input = sys.stdin.readline

def dprintn(str,val):
    if DEBUG : print(str,'=',val, end=" , ")

def dprint(str,val):
    if DEBUG : print(str,'=',val)

def printYes():
    print('Yes')
    exit()

def printNo():
    print('No')
    exit()

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

def input_list_2d_dict(lines):
    dat=[]
    datlist=set()
    datdict={}
    for yy in range(lines):
        values = list(map(int,input().split()))
        dat.append(values)
        datlist.add(values[0])
        datlist.add(values[1])

    return(dat,datlist)

DEBUG=False
# DEBUG=True

inp = input_list()
N = inp[0]
M = inp[1]
dprintn('N',N)
dprint('M',M)

dat = [[] for i in range(N)]
dprint('dat',dat)
datlist=set()
datdict={}
for yy in range(M):
    values = list(map(int,input().split()))
    val0 = values[0] - 1
    val1 = values[1] - 1
    if len(dat[val0])>2:
        printNo()
        exit()
#    elif val1 in dat[val0]:
#        printNo()        
#        exit()
    else:
        dat[val0].append(val1)
        dat[val1].append(val0)
    datlist.add(val0)
    datlist.add(val1)

dprint('dat',dat)
dprint('datlist',datlist)

if M == 0:
    printNo()
    exit()

if N == M:
    printNo()
    exit()

if N != M+1:
    printNo()
    exit()

cnt = 0
ptr = 1
datlist.remove(ptr)
for ii in range(N):
    dprintn('ii',ii)
    dprintn('ptr',ptr)
    dprintn('datlist',datlist)
    if len(dat[ii]) == 1:
        break
## ここまでそっくり
## ここから書き換え
import collections
dq = collections.deque()
visited = set()
dq.append(ii)
visited.add(ii)
while dq:
    i = dq.popleft()
    if len(dat[i]) > 2:
        break
    for next in dat[i]:
        if next not in visited:
            dq.append(next)
            visited.add(next)
if len(visited) == N:
    printYes()
else:
    printNo()