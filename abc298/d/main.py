from collections import defaultdict, deque, Counter
MOD=998244353
import sys
input = sys.stdin.readline
Q=int(input())

dq = deque()
dq.append(1)
sum = 1
keta = 1
for ii in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        dq.append(q[1])
        sum = (sum*10 + q[1])%MOD
        keta += 1
    elif q[0] == 2:
        val = dq.popleft()
        sum -= pow(10,keta-1,MOD)*val
        sum %= MOD
        keta = keta-1
    elif q[0] == 3:
        print(sum%MOD)
