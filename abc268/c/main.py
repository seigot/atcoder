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
N = int(input())
p = list(map(int, input().split()))
#print(p)
d = defaultdict(int)
for ii in range(len(p)):
    pp = p[ii]
    person = ii
    # この料理が期待するpersonの前に来るのに何回回転が必要か
    turn_num = (pp - person) % N
    #print(turn_num)
    
    # 投票する
    d[turn_num] += 1
    d[(turn_num + 1)%N ] += 1
    d[(turn_num - 1)%N ] += 1

#print(d)
ans = max(d.values())
print(ans)