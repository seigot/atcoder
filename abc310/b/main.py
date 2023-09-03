#!/usr/bin/env python3                                                                          
N,M=map(int, input().split())
PCF=[list(map(int, input().split())) for _ in range(N)]

S = set()
PCF = sorted(PCF, key=lambda x: x[0],reverse=True)

pre_price = 0
pre_n = 0
for l in PCF:
    price = l[0]
    n = l[1]
    comb = l[2:]
    bit = 0
    for ii in comb:
        bit += 1 << ii
    for s in S:
        if bit & s == s:
            if pre_price > price or pre_n < n:
                print("Yes")
                exit()
    pre_price = price
    pre_n = n
    S.add(bit)
print("No")
