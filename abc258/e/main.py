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

N, Q, X = map(int, input().split())
W = list(map(int, input().split()))
accumW = [0] + W

# 累積和(Wの累積和)
for i in range(N):
    accumW[i+1] += accumW[i]

# lからrまでの重さの和
# sum(W[l] + ... + W[r])
def wrangeSum(l, r):
    return accumW[r+1] - accumW[l]
# nowからxまでの重さの和
# sum(W[now] + W[now+1] + ... +  W[now+x-1])
def wsum(now, x):
    if x == 0: return 0
    l, r = now, now + x - 1
    if N <= r:
        return wrangeSum(l, N-1) + wrangeSum(0, r % N)
    else:
        return wrangeSum(l, r)

Wsum = sum(W)       # Wの合計値
done = [False] * N  # 探索済みかどうか
nxt = [-1] * N      # 次のindex(Functional Graph)
weight = [-1] * N   # じゃがいもの個数
ans = []            # index

now = 0
while not done[now]:
    done[now] = True
    # rest: Wの周期+α必要な重さ, take:周期を超えた際のじゃがいもの個数
    rest = X % Wsum
    take = X // Wsum * N

    # 二分探索する
    bottom, top = 0, N
    while top - bottom > 1:
        mid = (top + bottom) // 2
        if wsum(now, mid) < rest:
            bottom = mid
        else:
            top = mid
    if rest == 0:
        # restが0の場合はtopが少しずれるので修正..
        top = 0
    take += top
    weight[now] = take           # now番目から始まった際はtake個のじゃがいもを取得する
    ans.append(now)              # now番目のindex
    nxt[now] = (now + top) % N   # now番目の次のindex
    now = nxt[now]               # 次のindexを探す、これを周期にハマるまで繰り返す

# 全てのクエリについて解く
period_begin = ans.index(now)    # 周期の始まりのindexを取得(最初から周期が始まるわけではなくどこかから周期が始まる)
period = len(ans) - period_begin # 周期の長さ
for _ in range(Q):
    # 全てのクエリ
    k = int(input())
    # 0-index
    k -= 1
    if k < len(ans):
        print(weight[ans[k]])
    else:
        # ansの配列を超える場合は周期に入るので周期を考慮する
        k -= period_begin   # 周期の始まりに合わせる(%=periodのため)
        k %= period         # 割り算
        k += period_begin   # 戻す
        print(weight[ans[k]])
