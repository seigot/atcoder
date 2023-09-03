#https://atcoder.jp/contests/ABC317/tasks/ABC317_d 
import sys
sys.setrecursionlimit(5*10**5)
input = sys.stdin.readline
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush
from bisect import bisect_left, bisect_right
from math import gcd


n = int(input())
xyz = [list(map(int,input().split())) for i in range(n)]
tot = 0
# 座席数の合計を計算
for i in range(n):
    tot += xyz[i][-1]
# dp[N]: N個の席を確保する際の最小のコスト
# dp[ii][jj]: ii個目までのエリアに着目した時、jjの席を確保する際の最小のコスト
dp = [10**15]*(tot+1)
dp[0] = 0
ans = 10**15
# 最初のものからN個分を計算する
for ii in range(n):
    x,y,z = xyz[ii]
    # 順番に遷移する
    new = [10**15]*(tot+1)
    for jj in range(tot+1): ## jj席獲得するために必要な最小コストを更新する
        new[jj] = dp[jj]
        if jj - z >= 0:
            # z席を獲得する場合の最小コストを更新する
            need = (x+y+1)//2    # 必要な席数
            lack = max(0,need-x) # 必要なコスト
            new[jj] = min(new[jj], dp[jj-z] + lack) # 更新
        if jj > (tot/2):
            # jj席獲得することを考えた時に、過半数を超えていたら回答を更新する
            ans = min(ans, new[jj])
    dp = new
print(ans)