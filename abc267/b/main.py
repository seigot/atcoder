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

S = input()

# pin1が立っている(=1)場合はスプリットではない
if S[0] == "1":
    print("No")
    exit(0)

# 全部倒れる場合のチェック
l = [[7],[4],[2,8],[1,5],[3,9],[6],[10]]
for ii in range(1,len(l)-1):

    CHECK="NO"
    # 全部倒れている列を見つける
    for jj in l[ii]:
        #print(jj-1,S[jj-1])
        if S[jj-1] == "1":
            CHECK="YES"

    #print(ii, l[ii], CHECK)
    if CHECK == "YES":
        # どれか１つでも倒れていたらスキップ
        continue

    # 倒れている場合は前後の列をチェック
    # PINが一本でも立っていればOK
    for hh in range(1,ii+1):
        #print(hh)
        for jj in l[ii-hh]:
            if S[jj-1] == "1":
                for ll in range(1,7-ii-1+1):
                    #print(ll)
                    for kk in l[ii+ll]:
                        if S[kk-1] == "1":
                            print("Yes")
                            exit(0)

print("No")
