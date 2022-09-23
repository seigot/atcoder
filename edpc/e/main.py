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

N,W=map(int, input().split())

wv = []
wv.append((0,0))
for ii in range(N):
    w, v = map(int, input().split())
    wv.append((w,v))

# dp[i][j]
#    : i番目までのお菓子で、価値がjとなるものの中での重さが最小値となるのやつ
#    # 重さのMAXが10**9なので、配列を作ることができない

M = 10**5+100
dp = [[INF]*(M) for ii in range(N+1)]
dp[0][0] = 0

# 探索
for ii in range(1,N+1):
    # 価値
    for jj in range(0, M):
        ## 品物iiに着目
        if jj-wv[ii][1] >= 0:
            dp[ii][jj] = min(
                dp[ii-1][jj],                               # 何も選択しない場合
                dp[ii-1][jj-wv[ii][1]] + wv[ii][0]          # 該当(ii)のお菓子を選択する場合の重さ
            )
        else:
            dp[ii][jj] = dp[ii-1][jj]

#print(dp)
ans = 0
for ii in range(1, N+1):
    for jj in range(len(dp[N])):
        if dp[ii][jj] <= W:
            # 重さがW以下のものの中で価値が一番高いやつ
            ans = max(ans, jj)
print(ans)
