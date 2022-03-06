mod=998244353
n=int(input())
dp=[[0]*10 for _ in range(n)]
dp[0]=[1]*10   # 1-9

for i in range(1,n):   # 1-3
    for j in range(1,10): # 1-9

        # 1
        # 1->12
        # 1->12->121
        # 1->12->121->1211 ..のように変換できるものがどれだけあるか投票していく

        # 桁数iの、数値(j-1)から投票される値の数
        # (j!=0)の場合をケアする
        if j==1:
            dp[i][j]+=dp[i-1][j] + dp[i-1][j+1]
        elif j==9:
            dp[i][j]+=dp[i-1][j-1] + dp[i-1][j]
        else:
            dp[i][j]+=dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
        # overflow防止(どこで実行しても同じだが早めにmodしておく)
        dp[i][j]%=mod

# print(dp[i])
print(sum(dp[n-1])%mod)
