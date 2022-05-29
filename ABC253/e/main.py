MOD = 998244353
N, M, K = map(int, input().split())

# 長さiで最後がjなやつの個数
dp = [[0] * (M+3) for _ in range(N)]

# 初期化
for j in range(1, M+1):
    dp[0][j] = 1

# 探索(動的計画法)
for i in range(1, N):

    # 累積和
    accum = dp[i-1]
    for j in range(1, M+3):
        accum[j] += accum[j-1]
        accum[j] %= MOD

    # i時点のjの場合の数を計算する
    for j in range(1, M+1):
        # 一回加算してから差分をとる
        dp[i][j] = (accum[M] - accum[0])
        if K != 0:
            # min,maxを番兵にする
            dp[i][j] -= (accum[min(M, j+K-1)] - accum[max(j-K, 0)])
        dp[i][j] %= MOD
    #print(accum)

# 一番最後のdpのsum
print(sum(dp[-1]) % MOD)
