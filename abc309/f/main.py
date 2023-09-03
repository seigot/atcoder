from collections import defaultdict

#!/usr/bin/env python3                                                                          
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(4100000)
import math
import os
from inspect import currentframe
ONLINE_JUDGE = os.environ["HOME"] == "/home/contestant"
def error1(*args, end="\n"): # 変数のみ表示
    if ONLINE_JUDGE: return
    print("[stderr]", *args, end=end, file=sys.stderr)
def error(*args): # 変数の名前と値をまとめて表示
    if ONLINE_JUDGE: return
    names = {id(v): k for k, v in currentframe().f_back.f_locals.items()}
    print("[stderr]",' '.join([names.get(id(arg), '???') + ' = ' + repr(arg) for arg in args]), file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from math import gcd
from itertools import permutations,combinations
from copy import deepcopy
dpos2 = ((1, 0), (0, 1))
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos4cross = ((1, 1), (1, -1), (-1, 1), (-1, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
MOD = 998244353
def invmod(a):
    return pow(a,-1,MOD)
INF = float("inf")
MINF = -float("inf")

from math import gcd
from bisect import bisect_left, bisect_right
from heapq import heappop, heappush
from collections import defaultdict, deque, Counter
import sys
sys.setrecursionlimit(5*10**5)
input = sys.stdin.readline

# -----
def add(x, y):
    return x + y

def e(a):
    if a == min:
        return 10**18
    if a == max:
        return -10**18
    if a == add:
        return 0

class SegTree:
    def __init__(self, segf, init_val):
        # 初期化
        # 引数1:区間の最小/最大の値を返す(min/max)
        # 引数2:区間の配列初期値（ex.最小にする場合は[10**18]*n）
        n = len(init_val)
        self.segf = segf
        self.e = e(segf)
        self.seg_len = 1 << n.bit_length()
        self.seg = [self.e] * 2*self.seg_len

        for i in range(n):
            self.seg[i + self.seg_len] = init_val[i]
        for i in range(self.seg_len)[::-1]:
            self.seg[i] = segf(self.seg[i << 1], self.seg[i << 1 | 1])

    def point_add(self, pos, x):
        # 位置posの値を更新する(x加算する)
        pos += self.seg_len
        self.seg[pos] += x
        while True:
            pos >>= 1
            if not pos:
                break
            self.seg[pos] = self.segf(
                self.seg[pos << 1],  self.seg[pos << 1 | 1])

    def point_update(self, pos, x):
        # 位置posの値を更新する(xにする)
        pos += self.seg_len
        self.seg[pos] = self.segf(self.seg[pos],x)
        while True:
            pos >>= 1
            if not pos:
                break
            self.seg[pos] = self.segf(
                self.seg[pos << 1],  self.seg[pos << 1 | 1])

    def get_range(self, l, r):
        # 区間（l,r）のmin/max/sumなどの値を取得する(segfに依存する)
        l += self.seg_len
        r += self.seg_len
        res = self.e
        while l < r:
            if l & 1:
                res = self.segf(res, self.seg[l])
                l += 1
            if r & 1:
                r -= 1
                res = self.segf(res, self.seg[r])
            l >>= 1
            r >>= 1
        return res

#    # ------ range_add & get_point -------
#    def range_add(self, l, r, x):
#        l += self.seg_len
#        r += self.seg_len
#        self.seg[l] += x
#        self.seg[r] += x
#        while l < r:
#            if l & 1:
#                self.seg[l] = self.segf(x, self.seg[l])
#                l += 1
#            if r & 1:
#                r -= 1
#                self.seg[r] = self.segf(x, self.seg[r])
#            l >>= 1
#            r >>= 1
#
#    def get_point(self, pos):
#        pos += self.seg_len
#        res = self.seg[pos]
#        while True:
#            pos >>= 1
#            if not pos:
#                break
#            res = self.segf(res, self.seg[pos])
#        return res

#l = (4,3,2,1)
#error(sorted(l))

n = int(input())
box = defaultdict(list)
xs = set()
ys = set()
for i in range(n):
    l = list(map(int,input().split()))
    x,y,z = sorted(l)     # 向きを合わせる、値を小さい順にかえる
    xs.add(x)
    ys.add(y)
    box[x].append((y,z))  # 向きを合わせた時のxyを保存

error(xs)
xs = list(sorted(xs))
xs = xs[::-1]
error(xs)

def compress(arr):
    *s, = set(arr)
    return {num: i for i, num in enumerate(sorted(s))}
error(ys)
compy = compress(ys)
error(compy) # 順番にする

# 引数1:区間の最小/最大の値を返す(min/max)
# 引数2:区間の配列初期値（ex.最小にする場合は[10**18]*n）
st = SegTree(min, [10**18]*n)

ok = 0
error(xs)
while xs:
    x = xs.pop()
    error(x)
    # xを昇順にみていった際に
    # これまでの区間の最小のzの値を取得し、現在のzがそれを超える値かどうかをチェックする
    # これまでの区間 = 今着目しているyよりも小さい区間
    for y,z in box[x]:
        compyy = compy[y]
        error(x,y,z,compyy)
        mini = st.get_range(0,compy[y])
        error("st.get_range", compy[y],mini,z)
        if mini < z:
            ok = 1
    # zの値を更新する
    for y,z in box[x]:
        error("st.point_update", compy[y], z)
        st.point_update(compy[y], z)


print('Yes') if ok else print('No')
    


