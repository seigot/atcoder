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

class SegmentTree:
    """0-indexed, [a,b)"""

    def __init__(self, N, func=min, ex=10**18) -> None:
        n = 1
        while n < N:
            n <<= 1

        self.n = n
        self.ex = ex  # 単位元
        self.elements = [ex] * (2 * n - 1)
        self.func = func  # 結合則を満たす

    def update(self, i, x):
        i += self.n - 1
        self.elements[i] = x
        while i > 0:
            i = (i - 1) // 2
            self.elements[i] = self.func(
                self.elements[i * 2 + 1], self.elements[i * 2 + 2]
            )

    def update_range(self, l, r, x):
        if type(x) in [int, float]:
            x = [x] * (r - l)
        l += self.n - 1
        r += self.n - 1
        self.elements[l:r] = x
        while 0 < l < r:
            l = (l - 1) // 2
            r = r // 2
            for i in range(l, r):
                self.elements[i] = self.func(
                    self.elements[i * 2 + 1], self.elements[i * 2 + 2]
                )

    def query(self, l, r):
        l += self.n - 1
        r += self.n - 1
        res = self.ex
        while l < r:
            if l % 2 == 0:
                res = self.func(res, self.elements[l])
                l += 1
            if (r - 1) % 2:
                res = self.func(res, self.elements[r - 1])
                r -= 1
            l = l // 2
            r = r // 2
        return res

    def get(self, i):
        return self.elements[i + self.n - 1]

    def show(self):
        res = []
        for i in range(self.n):
            res.append(self.query(i, i + 1))
        print(*res)

    def show_pyramid(self):
        i = 0
        while 1 << i <= self.n:
            print(self.elements[(2**i - 1) : (2 ** (i + 1) - 1)])
            i += 1


N = int(input())


def compress(L):
    S = sorted(set(L))  # 配列に含まれるユニークな要素
    d = dict()  # 要素の順位
    i = 0
    for s in S:
        d[s] = i
        i += 1
    ret = []
    for l in L:
        ret.append(d[l])

    return ret


H = []
W = []
D = []


for _ in range(N):
    h, w, d = sorted(map(int, input().split()))

    H.append(h)
    W.append(w)
    D.append(d)
error(H)
error(W)
error(D)
H = compress(H)
W = compress(W)
D = compress(D)
error(H)
error(W)
error(D)

HWD = defaultdict(list)
for h, w, d in zip(H, W, D):
    HWD[h].append((w, d))
error(HWD)
error(sorted(HWD))

st = SegmentTree(N + 1)

for h in sorted(HWD):
    error(h)

    for w, d in HWD[h]:
        error(w, d)
        if st.query(0, d) < w:
            print("Yes")
            exit()

    for w, d in HWD[h]:
        error(w, d)
        v = st.query(d, d + 1)
        error(v)
        if w < v:
            st.update(d, w)
            error(st)


print("No")
