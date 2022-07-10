import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict as dd


N=int(input())
ST=[list(input().split())  for _ in range(N)]
print(ST)

S2Score=dd(lambda:-1)
maxscore=0

# 探索
for i in range(N):
    S,T=ST[i]
    T=int(T)
    if S2Score[S]==-1:
        S2Score[S]=T
        maxscore=max(maxscore,T)

# 検索
for i in range(N):
    if S2Score[ST[i][0]]==maxscore:
        print(i+1)
        break
