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
# https://atcoder.jp/contests/abc272/submissions/35514040
# @lazylazy

# 以下により、計算量をO(NlogN)にする事がポイント
# # mnは探索範囲であり、該当の要素がマイナスである場合は正になるタイミングからカウントを始める
# # 最大値は高々Nなので、Nを超えた場合は無視する
def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # 回答用の配列（集合型）
    res = [set() for _ in range(M)]
    for i in range(N):
        # 配列の全要素に着目する
        # mnは探索範囲であり、該当の要素がマイナスである場合は正になるタイミングからカウントを始める
        mn = 1
        if A[i] < 0:
            mn = (abs(A[i])) // (i + 1)
#            mn = (-1*(A[i])) // (i + 1)

        for j in range(mn, M + 1):
            # i: 1回あたりに加算する値
            # j: j回目のことを考慮する際の係数値
            if A[i] + (i + 1) * j > N:
                # 最大値は高々Nなので、Nを超えた場合は無視する
                break
            # i番目に着目した際にj-1回目に存在する値を加算する
            res[j - 1].add(A[i] + (i + 1) * j)

    # 0~M-1回までそれぞれの値(非負整数のうち配列にない最大の整数)を探索する
    for i in range(M):
        for j in range(N + 1):
            if j not in res[i]:
                print(j)
                break

if __name__ == "__main__":
    main()

