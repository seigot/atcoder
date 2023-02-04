# -*- coding: utf-8 -*-
# ACx48 TLEx15

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

# 素因数分解
def factorization2(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
                arr.append(i)

    if temp!=1:
        arr.append(temp)

    if arr==[]:
        arr.append(n)

    return arr


K = int(input())
dprint('K',K)

soinsu = factorization2(K)
dprint('soinsu',soinsu)

if len(soinsu) == 1:
    print(K)
    exit()

# 素因数分解
aa = factorization2(K)
# 集合に変換
aa_set = set(aa)
# 集合の各要素に着目する
ans = []
for pn in aa_set:
  # 各要素の個数を数える
  pn_cnt = aa.count(pn)
  cnt = 0
  for n in range(pn, pn**pn_cnt+1):
    # 素因数がpn_cnt個含まれる最大の整数を見つける
    tn = n
    while tn%pn == 0:
      tn /= pn
      cnt += 1
    if cnt >= pn_cnt:
      ans.append(n)
      break
print(max(ans))
