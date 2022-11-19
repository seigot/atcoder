#!/usr/bin/env python3
import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# 各数値の個数抽出
d = defaultdict(int)
for a in A:
    d[a] += 1

# 個数の大きい順に出力
d_keys=sorted(d.keys(),reverse=True)
d_keys_len=len(d_keys)
for ii in d_keys:
    print(d[ii])
# 残りを出力
for ii in range(N-d_keys_len):
    print(0)
