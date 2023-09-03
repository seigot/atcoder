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
from heapq import heappop, heappush
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

import sys
sys.setrecursionlimit(5*10**5)
input = sys.stdin.readline
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush
from bisect import bisect_left, bisect_right
from math import gcd

n = int(input())
s = input()

# n未満の約数の集合を返す
# in : 正の整数n
# out: 約数(の集合set) 
def fact(n):
    l = set()
    for i in range(1,int(pow(n,0.5))+1):
        if n % i == 0:
            l.add(i)
            l.add(n//i)
    return l

fn = fact(n)
fn.discard(n)         # 今回はNは対象外
fn = sorted(list(fn)) # リスト化してsort()

kaku = []        # "."がある所の組み合わせ
cnts = [0]*(n+1) # 約数iの時の"."の数（今回は約数を求めた場合のみカウントする）
for i in fn:
    now = [0]*i
    # "."の出現場所を周期で割った余りを求める
    # (最低限この周期パターンが出ていればOKのようなもの)
    for j in range(n):
        now[j%i] |= (s[j] == ".")
    kaku.append(now)
    cnts[i] = sum(now)
error(fn)
error(kaku)
error(cnts)

# 全パターンを求める、重複を除く
ans = [0]*(n+1)
for i in range(len(fn)):
    # 約数分ループする、fn[i]に着目する
    gs = set()
    for j in range(i):
        # 該当のものと周期が重なっているかどうかを確認
        # （最大公約数を求める、1は絶対含む）
        g = gcd(fn[i], fn[j])
        gs.add(g)
    error(i,fn[i],gs)
    # 約数iの場合の全パターンを求める
    # (既に"."の部分は確定なので、"#"の部分("."を除く)の場合の数を全て求める)
    tmp = pow(2, fn[i]-cnts[fn[i]])
    # ただし重複となっているものを除く
    # 重複となっているものは、最大公約数となったものの場合の数ぶん存在する
    for num in gs:
        tmp -= ans[num]
    error(i,gs,tmp)
    # 約数fn[i]での答えはtmp個
    ans[fn[i]] = tmp

print(sum(ans)%MOD)