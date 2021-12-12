#!/bin/python

N = int(input())
#空のリスト
A = []
#リストAにappend()を使って格納していく
for _ in range(N):
    A.append(input())

max_cnt=0
max_str="test"
for _ in range(N):
    T = A[_]
    cnt = 0
    #print(T)
    for __ in range(N):
        if T == A[__]:
            cnt+=1
    if max_cnt < cnt:
        max_cnt = cnt
        max_str = T
        #print(max_str)

print(max_str)
