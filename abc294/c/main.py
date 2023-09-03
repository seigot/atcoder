#!/usr/bin/env python3                                                                          
import sys
input = sys.stdin.readline
sys.setrecursionlimit(4100000)
import math
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush
from math import gcd
from itertools import permutations,combinations
from copy import deepcopy
dpos2 = ((1, 0), (0, 1))
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N,M=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
A=set(map(int, input().split()))  # (5)リストで受け取り 入力例:A1 A2 ... An
B=set(map(int, input().split()))  # (5)リストで受け取り 入力例:A1 A2 ... An
AB = A | B
ansA = []
ansB = []
idx = 1
sortedAB = sorted(list(AB))
for v in sortedAB:
    if v in A:
        ansA.append(idx)
    else:
        ansB.append(idx)
    idx += 1
print(*ansA)
print(*ansB)
