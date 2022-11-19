n, m = map(int,input().split())
x = list(map(int,input().split()))
dp = [[-1 for _ in range(n+1)] for _ in range(n)]

bonus = [0] * (n+1)
for i in range(m):
    c, y = map(int,input().split())
    # bonusがない場合でもbonus=0とみなす
    bonus[c] = y

# i=0の場合
dp[0][0] = 0
dp[0][1] = x[0]+ bonus[1]
# i=1~n-1まで回す
for i in range(1, n):
    for j in range(i+1+1): # i回目に着目している時、表の出るパターンはi+1(裏が出る)通り
        if j == 0:         # 表を0回出した（裏を出した）時
            dp[i][0] = max(dp[i-1])
        else:              # 表をj(j>=1)連続で出した時
            dp[i][j] = dp[i-1][j-1] + x[i] + bonus[j] # i-1回目に、j-1連続だった時のスコアに足す。

print(max(dp[n-1]))