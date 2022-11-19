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
# current time   20:12:20
from collections import defaultdict
N, K = map(int, input().split())

sunuke_is_okashi = defaultdict(int)  # defaultdict使うパターン
#sunuke_is_okashi = [0] * (N+1)      # 配列使うパターン

for ii in range(K):
    dn = int(input())
    An = list(map(int, input().split()))
    for jj in range(dn):
        A = An[jj]
        sunuke_is_okashi[A] = sunuke_is_okashi[A] + 1

ans = N - len(sunuke_is_okashi.keys())  # keys()使うパターン
#ans = 0                                     # シンプルに数えるパターン
#for ii in range(1, N+1):
#    if sunuke_is_okashi[ii] == 0:
#        ans += 1
print(ans)