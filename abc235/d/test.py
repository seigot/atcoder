#!/bin/python

import sys
def error(*args, end="\n"): print("[log stderr]", *args, end=end, file=sys.stderr)
from collections import deque

# input
#l = list(map(int, input().split()))                     # a1, a2, a3... an
#l = [list(map(int, input().split())) for l in range(N)] # [[a1, b1], [a2, b2],... [aN, bN]]

a, N = map(int, input().split())

MAX = 10**7       # 配列のmax値, 10^6 より大きい数
Q = deque()       # deque()
Q.append((1, 0))  # 初期値を入れる。データは(値、階層)の組で管理する
cnt = [-1]*(MAX)  # 探索したかどうかを判断する用途

error(Q)
while Q:
    n, t = Q.popleft()

    # 幅優先探索

    # a倍する
    if n*a < MAX:
        # 未探索である場合
        if cnt[n*a] == -1:
            cnt[n*a] = t+1       # 探索した事を残す(最短でt+1回目で探索する事になる)
            Q.append((n*a, t+1)) # queueする

    # 1の位を先頭にもってくる(1の位が0ではない場合)
    if n%10:
        n2 = int(str(n)[-1]+str(n)[:-1])
        if n2 < MAX:
            # 未探索である場合
            if cnt[n2] == -1:
                cnt[n2] = t+1       # 探索した事を残す(最短でt+1回目で探索する事になる)
                Q.append((n2, t+1)) # queueする

print(cnt[N])

# output
# error(ans)
# for i in range(len(ans)):
#     error(ans)
