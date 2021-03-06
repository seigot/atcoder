#!/bin/python

#N, K = map(int, input().split())
#l = list(map(int, input().split()))
#
#sum = [0] * N
#for i in range(N):
#    #print(l[i])
#    if i == 0:
#        sum[i] = l[i]
#    else:
#        sum[i] = sum[ i-1 ] + l[i]

#print(N, K)
#print(l)
#print(sum)

#cnt = 0
#for i in range(N):
#    for j in range(0, N - i):
#
#        if j == 0:
#            diff = sum[i + j]
#        else:
#            diff = sum[i + j] - sum[i]
#
#        if diff == K:
#            cnt += 1

#for i in range(N):
#    for j in range(0, N - i):
#
#        if j == 0:
#            diff = sum[i + j]
#        else:
#            diff = sum[i + j] - sum[i]
#
#        if diff == K:
#            cnt += 1


from collections import *
from itertools import *
 
# Input #######################################
 
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
 
Aaccum = list(accumulate(A))
 
dict_Aaccum = defaultdict(int)
for a in Aaccum:
    dict_Aaccum[a] += 1

#print(dict_Aaccum)
print(Aaccum)

ans = 0
k = K
for i in range(N):
    # まずKの数を数える。これは１つだけで条件を満たす。
    # 次に連続部分列について考える。一番初めに着目した部分以降に、着目した部分のまで数値+Kの値があれば条件を満たす。
    # これを繰り返す。

    # もしKが存在したら、存在する個数だけ答えに加算
    if k in dict_Aaccum:
        ans += dict_Aaccum[k]
    # いま見ている箇所はもう使わないので-1カウントする
    dict_Aaccum[Aaccum[i]] -= 1
    # kを更新する
    k += A[i]
 
print(ans)

#print(cnt)
