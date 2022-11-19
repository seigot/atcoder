import bisect, collections, copy, heapq, itertools, math, string
import random
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
from collections import deque
from collections import Counter
from collections import defaultdict
import bisect
from functools import reduce

def main():
    N, M = MI()
    towns_treasures = []
    INF = 10 ** 12
    for i in range(N):
        x,y = MI()
        towns_treasures.append((x, y))
    for i in range(M):
        p,q = MI()
        towns_treasures.append((p,q))

    # bitDP用の配列を用意する
    # dp[i][j] : iまでの集合に着目したときに最後がjのもののうち最小コストをいれるやつ、iはbit列、jは各点 bit列-->各点へ移動する際の最小コストを格納する
    dp = [[INF] * (N+M) for _ in range(2**(N+M))]
    for i in range(N+M):
        dp[1 << i][i] = ((towns_treasures[i][0]**2) + (towns_treasures[i][1]**2))**0.5
    # N+Mの全組み合わせのコストを算出する
    Cost = [[0] * (N+M) for _ in range(N+M)]
    for i in range((N+M)):
        for j in range((N+M)):
            Cost[i][j] = (((towns_treasures[j][0] - towns_treasures[i][0])**2) + (towns_treasures[j][1] - towns_treasures[i][1])**2)**0.5

    mask = (1 << N) - 1
    ans = INF
    for s in range(1 << (N + M)):
        now_speed = 1
        # スピードアップ
        for past in range(N, N + M):
            if (s >> past) & 1:
                # 宝箱を通っている場合はスピードアップする(コストが下がる)
                now_speed *= 2
        # nowのループ
        for now in range(N + M):
            if s & mask == mask:
                # Nを全て通っている場合に更新する
                ans = min(ans, 
                          dp[s][now] + (((towns_treasures[now][0]**2) + (towns_treasures[now][1]**2))**0.5)/now_speed)
                continue
            # nextのループ
            for next in range(N + M):
                    s_next = s | (1 << next)
                    dp[s_next][next] = min(dp[s_next][next], dp[s][now] + Cost[now][next]/now_speed)

    print('{:.10f}'.format(ans))

if __name__ == "__main__":
    main()
