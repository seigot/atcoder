from cgi import MiniFieldStorage
import sys
sys.setrecursionlimit(4100000)
import math
import itertools
import collections
INF = float('inf')
MINF = -float('inf')
from heapq import heapify, heappop, heappush
from bisect import bisect, bisect_left, bisect_right
MOD = 10 ** 9 + 7
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from collections import defaultdict, deque

S = defaultdict(int)
s = set()
minval = 0
maxval = 0
N=int(input())                     # (1)数字が1つ 入力例:N
for i in range(N):
    A=list(map(int, input().split()))  # (5)リストで受け取り 入力例:A1 A2 ... An
#    error(S)
#    error(A)
    if A[0] == 1:
        x = A[1]
        S[x] += 1
        s.add(x)
        if len(S) == 1:
            minval = x
            maxval = x
        else:
            minval = min(x, minval)
            maxval = max(x, maxval)

    elif A[0] == 2:
        x = A[1]
        c = A[2]
        if x in s:
            diff = min(c, S[x])
            S[x] -= diff
            if S[x] == 0:
                # update min,max
                del S[x]
                s.remove(x)
                if x == minval:
                    if len(s) == 0:
                        minval = MINF
                    else:
                        minval = min(s)
                if x == maxval:
                    if len(s) == 0:
                        maxval = INF
                    else:
                        maxval = max(s)
    else:
        print(maxval - minval)
#    error(minval, maxval)
