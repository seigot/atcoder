import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
dp = [[0, 0] for _ in range(N)]
ans = 10 ** 9 * N

# A0を行わない
dp[0][0] = 0
dp[0][1] = 10 ** 9 * N

for i in range(1, N):
    dp[i][0] = dp[i - 1][1]                           #ANを行わない
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + A[i] #ANを行う(事前にA[N-1]を行った方の小さい方のスコアを獲得できる事が期待値)
ans = dp[-1][1]

# A0を行う
dp = [[0, 0] for _ in range(N)]
dp[0][0] = 10 ** 9 * N
dp[0][1] = A[0]

for i in range(1, N):
    dp[i][0] = dp[i - 1][1]                           #ANを行わない(A[N-1]を行った際のスコアと同じ)
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + A[i] #ANを行う(事前にA[N-1]を行った方の小さい方のスコアを獲得できる事が期待値)
ans = min(ans, dp[-1][0], dp[-1][1])

print(ans)

