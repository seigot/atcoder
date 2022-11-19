n,m,k = map(int,input().split())
mod = 998244353
minv = pow(m, mod-2, mod)
#minv = pow(m, -1, mod)
#print(mm)
# dp[K][N] を、ルーレットを i 回回したときにマス j にいる確率と定義
dp = [[0]*(n+1) for i in range(k+1)]
# 0回目の時は0
dp[0][0] = 1

ans = 0
# 試行回数
for i in range(k):
  # 各マス目にいる場合に着目
  for j in range(n):
    # 目の値
    for num in range(1,m+1):
      if num + j<= n:
        # 前に進むケース
        dp[i+1][j+num] += dp[i][j]*minv %mod
        dp[i+1][j+num] %=mod
      else:
        # 折り返すケース(num+j > n)
        # 超えた分だけおりかえす、        
        dp[i+1][2*n-(j+num)] += dp[i][j]*minv %mod
        dp[i+1][2*n-(j+num)] %=mod

ans = 0
# 1回目〜K回目のトライでそれぞれゴールしている回数(確率)をカウント
for i in range(1, k+1):
  ans += dp[i][-1]
  ans %= mod
print(ans)