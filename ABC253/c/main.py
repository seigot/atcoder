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
        x = q[1] 
        if x  in st:
            s[x] += 1
        else:
            s[x] = 1
            st.add(x)
        _min = min(x, _min)
        _max = max(_max, x)
    elif q[0] == 2:
        x = q[1] 
        c = q[2] 
        if x in st:
            m = min(c, s[x])
            if m == s[x]:
                s.pop(x)
                st.remove(x)
                if _min == x:
                    if len(st) > 0:
                        _min = min(st)
                    else:
                        _min = inf
                if _max == x:
                    if len(st) > 0:
                        _max = max(st)
                    else:
                        _max = minf
            else:
                s[x] -= m
    else:
        print(_max - _min)
