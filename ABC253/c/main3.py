import sys
inputSys = sys.stdin.readline
# sys.setrecursionlimit(10**7)
from copy import deepcopy
import itertools  # combinations() <- nCr, permutations() <- nPr
import bisect  # 二分探索
import math  # factorial() <- 階乗, sqrt() <- 平方根
from functools import lru_cache # <- メモ化再帰 @lru_cache
import string
mod = 998244353
mod2 = 1000000007
inf = float("inf")
minf = -float("inf")
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
# lst.sort(key=lambda x: x[N]) <- N番目の要素でソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[0]) <- 辞書のkeyでソート
# sorted_lst = sorted(lst.items(), key=lambda x: x[1]) <- 辞書のvalueでソート



n = int(inputSys())
s = {}
st = set()
_min = inf
_max = minf

for i in range(n):
    q = list(map(int, inputSys().split()))
    if q[0] == 1:
        if q[1] in st:
            s[q[1]] += 1
        else:
            s[q[1]] = 1
            st.add(q[1])
        if q[1] < _min:
            _min = q[1]
        if q[1] > _max:
            _max = q[1]
    elif q[0] == 2:
        if q[1] in st:
            m = min(q[2], s[q[1]])
            if m == s[q[1]]:
                s.pop(q[1])
                st.remove(q[1])
                if _min == q[1]:
                    if len(st) > 0:
                        _min = min(st)
                    else:
                        _min = inf
                if _max == q[1]:
                    if len(st) > 0:
                        _max = max(st)
                    else:
                        _max = minf
            else:
                s[q[1]] -= m
    else:
        print(_max - _min)
