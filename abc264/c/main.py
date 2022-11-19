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
H1,W1=map(int, input().split())
A = []
for ii in range(H1):
    AA = list(map(int, input().split()))
    A.append(AA)
#print(A)
H2,W2=map(int, input().split())
B = []
for ii in range(H2):
    BB = list(map(int, input().split()))
    B.append(BB)
#print(B[1][2]) B[y][x]
#print(B)

# 行列Aが行列Bより大きい場合
#if H1 < H2 or W1 < W2:
#    print("No")
#    exit(0)

# 行列Aが行列Bより小さい場合
# 行列Aの部分集合が、行列Bとなるかどうか全探索
ans = "No"
from itertools import combinations
l = list(range(W1))
for cc in combinations(l, W2):
    # combinationの数だけ探索する
    #print(cc)
    #print(cc[1])
    #print(cc[2])
    #print(cc[3])
    jj_b = 0
    for jj_a in range(H1):
        # 縦
        check = True
        for ii_b in range(W2):
            ii_a = cc[ii_b]
            if A[jj_a][ii_a] != B[jj_b][ii_b]:
                # 不一致
                check = False
        if check == True:
            jj_b += 1
        if jj_b == H2:
            ans = "Yes"
            print(ans)
            exit(0)

print(ans)







