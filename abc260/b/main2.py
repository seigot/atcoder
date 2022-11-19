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
N,X,Y,Z=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))

# 合格者
passed_exam_idx = set()
#passed_exam_idx = []

# result
exam_result = []
for ii in range(N):
    # 0-index
    exam_result.append([ii, -1*A[ii], -1*B[ii], -1*(A[ii]+B[ii])])
#print(exam_result)

# math X
exam_result.sort(key=lambda exam_result: exam_result[0])
exam_result.sort(key=lambda exam_result: exam_result[1])
cnt = 0
for ii in range(N):
    # 上から順番
    id = exam_result[ii][0]
    if id in passed_exam_idx:
        continue
    if cnt == X:
        break
    passed_exam_idx.add(id)
    #passed_exam_idx.append(id)
    cnt += 1
#print(passed_exam_idx)

# english Y
exam_result.sort(key=lambda exam_result: exam_result[0])
exam_result.sort(key=lambda exam_result: exam_result[2])
cnt = 0
for ii in range(N):
    # 上から順番
    id = exam_result[ii][0]
    if id in passed_exam_idx:
        continue
    if cnt == Y:
        break
    passed_exam_idx.add(id)
    #passed_exam_idx.append(id)
    cnt += 1
#print(passed_exam_idx)

# total Z
exam_result.sort(key=lambda exam_result: exam_result[0])
exam_result.sort(key=lambda exam_result: exam_result[3])
#print(exam_result)
cnt = 0
for ii in range(N):
    # 上から順番
    id = exam_result[ii][0]
    if id in passed_exam_idx:
        continue
    if cnt == Z:
        break
    passed_exam_idx.add(id)
    #passed_exam_idx.append(id)
    cnt += 1
#print(passed_exam_idx)

#passed_exam_idx.sort()
for ii in sorted(passed_exam_idx):
    print(ii+1)
