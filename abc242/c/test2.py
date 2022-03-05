mod=998244353
n=int(input())
dp=[[0]*9 for _ in range(n)]
dp[0]=[1]*9

for i in range(1,n):   # 1-3
    for j in range(9): # 0-8

        # 更新
        if j-1>=0:
            dp[i][j]+=dp[i-1][j-1]

        # 更新
        dp[i][j]+=dp[i-1][j]

        # 更新
        if j+1<9:
            dp[i][j]+=dp[i-1][j+1]

        dp[i][j]%=mod

# print(dp[i])
print(sum(dp[n-1])%mod)
