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

S = []
for ii in range(9):
    s = input()
    S.append(s)
#print(S)

ans = 0
s = set()
# a全探索
for a_row in range(9):
    for a_virt in range(9):
        # b全探索
        for b_row in range(a_row,9):
            for b_virt in range(9):

                if a_row == b_row and a_virt == b_virt:
                    continue

                # 正方形の候補
                if S[a_row][a_virt] == '#' and S[b_row][b_virt] == '#':
                    c_row = b_row + (b_virt - a_virt)
                    c_virt = b_virt - (b_row - a_row)
                    d_row = a_row + (b_virt - a_virt)
                    d_virt = a_virt - (b_row - a_row)
                    if 0 <= c_virt < 9 and 0 <= c_row < 9 and 0 <= d_virt < 9 and 0 < d_row <= 9:
                        if S[c_row][c_virt] == '#' and S[d_row][d_virt] == '#':
                            #print((a_row, a_virt), (b_row, b_virt), (c_row, c_virt), (d_row, d_virt))
                            a = []
                            a.append(a_row+10*a_virt)
                            a.append(b_row+10*b_virt)
                            a.append(c_row+10*c_virt)
                            a.append(d_row+10*d_virt)
                            sa = sorted(a)
                            s.add((sa[0],sa[1],sa[2],sa[3]))
#                            ans += 1
#print(ans)
print(len(s))
