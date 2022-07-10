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

input = sys.stdin.readline

N = int(input())
XYP = [[int(x) for x in input().split()] for _ in range(N)]
ans = float("inf")

def can_jump(i, j, s):
    return XYP[i][2] * s >= abs(XYP[i][0] - XYP[j][0]) + abs(XYP[i][1] - XYP[j][1])

def is_ok(mid):
    # 全探索
    for ii in range(N):
        # 該当番号(ii)のジャンプ台に着目した時に、
        # 各ノードに辿り着けるかどうかチェックする（幅優先探索によりチェック）
        target_q = [ii]
        visited_s = set()
        visited_s.add(ii)
        while target_q:
            target = target_q.pop(0)
            # targetからジャンプ可能なジャンプ台を全探索で調べる
            for jj in range(N):
                if jj == target:
                    ## 自身の場合はスキップ
                    continue
                if jj in visited_s:
                    ## 探索済の場合はスキップ
                    continue
                # 未探索のジャンプ台を調べる
                # midの訓練を行なっている前提
                is_can_jump = can_jump(target, jj, mid)
                if is_can_jump == True:
                    ## targetジャンプから、対象のジャンプ台へジャンプ可能の場合は探索先のキューに加える
                    visited_s.add(jj) # 探索済
                    target_q.append(jj)    # 次の探索先
        if len(visited_s) == N:
            # 全てにvisitedになったならばTrue
            return True

    # 全てにvisitedにならない場合はFalse
    return False

# 二分探索
ok = 10**10
ng = 0
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)


