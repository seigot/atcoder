#!/bin/python

N, M = map(int, input().split())
#P = [input().split() for i in range(N)]
P = [list(map(int,input().split())) for _ in range(N)]

sorted_list = sorted(P, reverse=True)
len_s = len(sorted_list)
#print(N, M)
#print(sorted_list)

answer = 0
weight = 0
for i in range(N):
    A = int(sorted_list[i][0])
    B = int(sorted_list[i][1])
    print(A, B)

    diff = min(B, M - weight)
    weight += diff
    answer += A * diff
    if weight >= M:
        break

#print(weight)
print(answer)
