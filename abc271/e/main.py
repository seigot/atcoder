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

def main():

    N, M, K = map(int, input().split())
    ABC = []
    for _ in range(M):
        A, B, C = map(int, input().split())
        # 0-index
        A -= 1
        B -= 1
        ABC.append((A, B, C))
    # 部分列(0-index)
    E = list(map(lambda x: int(x) - 1, input().split()))

    # dp[i][u]:= 都市 1 から都市 u へ行く経路であって、
    #            通る道の番号を並べた列が (E1,…,Ei) の部分列になるようなものに対する、通る道の長さの合計の最小値。
    #            今回はuが固定なので、省略する

    dp = [INF] * N
    dp[0] = 0      # 道の出発点
    
    # eを順番にチェックする
    for ii in range(len(E)):
        e = E[ii]
        (a, b, c) = ABC[e]

        # 道の経路(1-->b)に対してコスト最小値を保存
        # 既存の経路 or 新たな経路(a-->cに来た時によりコストが低いケース)
        # Eの最初からこれを更新すればなんと正解を得られる！！
        # dp[a]が求まっていたら、答えの候補としてあり得る
        # dp[a]が求まっていない場合は、更新不要（答えがEの部分列にならないため）
        dp[b] = min(dp[b], dp[a] + c) 
    
    if dp[N-1] == INF:
#    if dp[-1] == INF:
        print(-1)
    else:
        print(dp[-1])

if __name__ == "__main__":
    main()