#!/usr/bin/env python3
import sys
sys.setrecursionlimit(4100000)
import math
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

# A,B=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
N = int(input())

Nbit = [] # Nを2進数とみたときにbitが1であるもの
Nbit1 = [] # Nを2進数とみたときにbitが1であるもの
Nbit0 = [] # Nを2進数とみたときにbitが0であるもの

# bitが立っているものを求める
val = N
k = 0
bit1keta = 0
while True:
    remain = val%2 # 余り
    sho = val//2   # 商
    val = sho
    Nbit.append(remain)
    bit1keta += 1
    k += 1
    if remain == 1:
        Nbit1.append(k)
    else:
        Nbit0.append(k)
        bit1keta -= 1        
    if sho == 0:
        break

#print(Nbit)
#print("Nbit1:", Nbit1)
#print("Nbit0:", Nbit0)
#print("bit1keta:", bit1keta)

Nbit1_elem = []
for ii in range(len(Nbit1)):
    val = 2**(Nbit1[ii]-1)
    Nbit1_elem.append(val)
#print(Nbit1_elem)

#print("---")
# count
for ii in range(2**bit1keta):

    ans = 0
    keta = 0
    val = ii
    while True:
        remain = val%2 # 余り
        sho = val//2   # 商
        val = sho
        if remain == 1:
            ans += Nbit1_elem[keta]
        if sho == 0:
            break
        keta += 1

    #print(ii, ans)
    print(ans)
    #print(str(bin(ii))[2:])   
    #ans = bin(ii)





