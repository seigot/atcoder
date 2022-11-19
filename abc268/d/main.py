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
N,M=map(int, input().split())  
S = [] 
S_len = 0
T = []
Tdict = defaultdict(int)
for ii in range(N):
    s = input()
    S.append(s)
    S_len += len(s)
for ii in range(M):
    s = input()
    T.append(s)
    Tdict[s] = 1
#print(S)
#print(S_len)
#print(T)

# N = 1
if N == 1:
    s = S[0]
    if  len(s) < 3:
        print(-1)
        exit(0)
    for ii in range(M):
        if s == T[ii]:
            print(-1)
            exit(0)
    print(s)
    exit(0)

# N = 2~8
from itertools import permutations 
from itertools import combinations_with_replacement
for p in permutations(list(range(N))):

    # 候補の文字列
    #cand = ""

    # Nの文字の組み合わせ
    # P
#    print(p)
    # _の組み合わせ
#    UnderlineMaxNum = 16 - S_len
#    print(UnderlineMaxNum)
    #UnderlineMaxNum = 16 - S_len 
    for j in range(16 - (S_len+ N - 1) + 1):
    #for jj in range(1, UnderlineMaxNum+1):

        for k in combinations_with_replacement(range(N - 1), j):

            cand = ""
#        # underlineをjj個使うパターン
#        if jj < N - 1:
#            # あるべき_の数より小さい場合はスキップ
#            continue
#
#        # jjをどこに何個使うか
#        # jj = 1~15くらいは想定される
#        njj = [1] * (N-1)
#        if jj - (N-1) > 0:
#            # 余りがある場合は余りを分配する
#            for k in combinations_with_replacement(range(N-1), jj - (N-1)):
            njj = [1] * (N-1)
            for kk in k:
                njj[kk] += 1

            cand += S[p[0]]
            for nn in range(N-1):
                cand += "_" * njj[nn]
                cand += S[p[nn+1]]

            #print(cand)
            # 3文字以上、16文字以下の制限
            # NG文字制限
            if Tdict[cand] > 0:
                continue
            print(cand)
            exit(0)
print(-1)
