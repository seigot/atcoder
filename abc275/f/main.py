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

n,m = map(int,input().split())
a = list(map(int,input().split()))
# https://atcoder.jp/contests/abc275/editorial/5140
# dp[i][j][k] を「a1b1+a2,b2 +…+aibi =j(iまでに着目して総和がjでなるやつ) かつ bi​ =k の時の操作回数の最小値
# dp[j][k] : 総和j となるために最小のもの(bi=1 or bi=0)
dp = [[INF, INF] for i in range(m+1)]
#dp = [[[INF, INF] for i in range(m+1)] for ii in range(n+1)]
#dp[0][0] = 1  # なにもbitを立てていない状態を初期化
dp[0][1] = 0   # 100000000...のbitが立っていて総和は0ですという意味
#dp[0][0][1] = 0   # 100000000...のbitが立っていて総和は0ですという意味

# anの各要素に着目
for i in range(1,n+1):
    # 更新用のリストを用意
    new = [[INF, INF] for i in range(m+1)] 
    # anの値を取得
    ai = a[i-1]
    # １つ前のDPを参考にして、総和をjにできるもののうち最小のものを更新する
    for j in range(m+1):
        # 場合分けする
        if j-ai >= 0:
            # k = 1(以降全部bitが1、以降全部bitが0)とする場合
            # 該当のビットを立てるケース
            # 総和が(j-ai)であり直前のbitが0の場合+ai --> (一見+1必要に見えるが右端なので)何もしない
            # 総和が(j-ai)であり直前のbitが1の場合+ai --> (bitが連続するので)何もしない
            # 元々、k = 0の場合は"以降全部bitが1としていたので過去どれかのケースに該当するはず"
            new[j][1] = min(dp[j-ai][0], dp[j-ai][1])
            #dp[i][j][1] = min(dp[i-1][j-ai][0], dp[i-1][j-ai][1])
        # 直前をみるケース
        # k = 0(該当bitは落として以降全部bitが0)とする場合
        # 該当のbitを立てないのであれば、
        # 総和が(j)であり直前のbitが0の場合 --> 何もしない
        # 総和が(j)であり直前のbitが1の場合 --> (0になる部分が増えるので)最小値を+1する
        # １つ前にビットを立てるもの+1(新しく該当部分の右側を0の部分列とするという意味)としたもの、のうち最小のものが答えとなる
        new[j][0] = min(dp[j][0], dp[j][1] + 1)
        #dp[i][j][0] = min(dp[i-1][j][0], dp[i-1][j][1] + 1)

    # dpを更新
    dp = new

# 結果を出力
# (最後に更新したdpの各iの最小回数に着目する)
for j in range(1, m+1):
    ans = min(dp[j])
    #ans = min(dp[n][j])
    if ans < INF:
        print(ans) 
    else:
        print(-1)
