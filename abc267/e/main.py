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
N,M=map(int, input().split())
A = list(map(int, input().split()))
UV = [[] for i in range(N+1)]
sums = [0]*(N+1)
# input
for ii in range(M):
    U,V = map(int, input().split())
    UV[U].append(V)
    UV[V].append(U)
    sums[U] += A[V-1] # 頂点U周りの合計値に加算
    sums[V] += A[U-1] # 頂点V周りの合計値に加算

# N 回の操作全体のコストを、1 回ごとの操作におけるコストのうちの最大値として定めます。操作全体のコストとして取り得る値の最小値を求めてください。
# --> 1回ごとの操作におけるコストのうちの最大値 = X とする

#print(UV)
from collections import deque
l = -1
r = max(sums) + 10
# 二分探索
while r - l > 1:
    # 中央値
    X = (l+r)//2
    # 初期化
    que = deque()
    cnt = 0
    pro = set()
    cp = [0]*(N+1)

    # 該当の頂点の合計値に着目する
    for i in range(1,N+1):
        cp[i] = sums[i] # tmp
        if sums[i] <= X:
            # 該当の頂点のまわりの合計値がX以下の場合, 該当の頂点をappend
            # ここは全部消せるはず
            que.append(i)
            pro.add(i)

    # queにあるもの全てをみる
    while que:
        crr = que.pop()
        cnt += 1
        for nxt in UV[crr]:
            if nxt in pro:
                # 探索済みの場合はcontinue
                continue
            # 未探索の場合は探索対象に加える

            # 該当の頂点を削除したとしたときに、ほかの辺の削除コストはA[crr-1]へる
            # この場合に頂点を消せそうであれば消しにかかる
            cp[nxt] -= A[crr-1]
            if cp[nxt] <= X:
                que.append(nxt)
                pro.add(nxt)

    # update
    if cnt != N:
        # Nに達しない場合はmが小さい可能性がある（より大きな値を考える）
        l = X
    else:
        # Nに達している場合はmが大きい可能性がある（より小さな値を考える）
        r = X
print(r)
 