#!/usr/bin/env python3
# https://atcoder.jp/contests/abc278/submissions/36650250
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

# dp[S][c]:= これまでに使っていない単語の集合が S⊆{s1,…,sN} であり、最後の文字が c である状態について、
# その状態から勝てるとき 1 、そうでないとき 0
# https://atcoder.jp/contests/abc278/submissions/36650775

from collections import defaultdict
N = int(input())
S = [input() for _ in range(N)]

# N文字存在するのでNbit分確保する
dp = [defaultdict(int) for _ in range(2 ** N)]

# bitDP
for i in range(1, 2 ** N):
  # 対象の文字列を取得する
  tmp_S = []
  for j in range(N):
    # iのj bit目に着目した場合にbitが立っている場合は探索対象に加える
    if i >> j & 1:
      tmp_S.append([j, S[j]])
  # 探索対象の文字列が存在する場合は探索する
  for j, s in tmp_S:
    # jは該当文字列のbit目(文字列の番号)
    # sは該当文字列そのもの
    if dp[i ^ (1 << j)][s[-1]] == 0:
      # 該当のbitを反転させた際（jが出ていない場合）に、sの末尾のものが残っていない場合は
      # 該当のiのうちsを取った場合に勝てるので1にしておく
      dp[i][s[0]] = 1
      # bitDPは再帰で求めるパターンもあるのか??
      # https://atcoder.jp/contests/abc278/submissions/36650250

# 全bitを探索した際にvaluesが1になる場合がある時はFirstがかち
ans = sum(dp[-1].values()) > 0
print('First' if ans else 'Second')
