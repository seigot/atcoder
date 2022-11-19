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

N, K = map(int, input().split())
A = list(map(int, input().split()))
#print(A)

# init
cnt = 0
X = 0
# 周期計算用
d = defaultdict(lambda:-1)
loop_length = 0
loop_sum = 0
loop_times = 0

for ii in range(K):
    # update
    X = cnt % N
#    print("--", X, A[X])
#    if False:
    if d[X] != -1:
        #print("cnt", cnt)
        #print(ii, d[X], X)
        # loop detected
        loop_length = ii - d[X]
        loop_times = (K - d[X]) // loop_length
        loop_times_mod = (K - d[X]) % loop_length
        # loop sum
        tmp_cnt = X
        for jj in range(loop_length):
            tmp_X = tmp_cnt % N
            a = A[tmp_X]
            tmp_cnt += a
        loop_sum = tmp_cnt - X
        # cnt
        #print(loop_length)
        #print(loop_times)
        #print(loop_times_mod)
        #print(loop_sum)
        #print("cnt", cnt)
        cnt += loop_sum * (loop_times-1) 
        #print("cnt", cnt)
        # 余り
        tmp_cnt = X
        for jj in range(loop_times_mod):
            tmp_X = tmp_cnt % N
            # add candy
            a = A[tmp_X]
            tmp_cnt += a
        cnt += (tmp_cnt - X)
        break
    else:
        d[X] = ii

    # add candy
    a = A[X]
    cnt += a

print(cnt)
