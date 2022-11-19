#!/usr/bin/env python3
import sys
sys.setrecursionlimit(4100000)
import math
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

# A,B=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
N = int(input())

MEMO = defaultdict(int)

def funcf(k):
    
    if k == 0:
        return 1

    val1 = k//2
    val2 = k//3

    # ans1
    if val1 == 0:
        ans1 = 1
    elif MEMO[val1] != 0:
        ans1 = MEMO[val1]
    else:
        ans1 = funcf(val1)
        MEMO[val1] = ans1

    # ans2
    if val2 == 0:
        ans2 = 1
    elif MEMO[val2] != 0:
        ans2 = MEMO[val2]
    else:
        ans2 = funcf(val2)
        MEMO[val2] = ans2

    return ans1 + ans2

ret = funcf(N)
print(ret)