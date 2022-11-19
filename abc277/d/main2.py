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

N,M=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
A=list(map(int, input().split()))  # (5)リストで受け取り 入力例:A1 A2 ... An

# 1.島を見つける
# 2.島ごとの数値の総和を求める
# 3.島ごとの数値の総和の総和 - max(島ごとの数値の総和)

# 1.
d = defaultdict(int)
A.sort()
#print(A)
for ii in range(N):
    a = A[ii]
    d[a] += 1
#print(d)
#print(d.keys())


# 2.
sums = set()
visited = set()
cnt = 0
ll = list(d.keys())
ll2 = list()

flag = 0
for ii in range(len(ll)):
    if ii == ll[ii]:
        pass
    else:
        ll2.append(ll[ii])
#print(ll2)

for targeti in ll2:
#    print(targeti)
    
    if targeti in visited:
        continue

    # 0を見つけたら次の添え字からどこまで島が続くか確認する
    if True:
        summ = 0
        for ii in range(0,M):
            # 次が0であるまで
            idx = (targeti+ii)%M
            if d[idx] == 0:
                break
            summ += idx*d[idx]
            visited.add(idx)
        sums.add(summ)
#print(sums)

# 3.
print(sum(sums)-max(sums))

