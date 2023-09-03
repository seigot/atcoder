from collections import defaultdict, deque, Counter
MOD = 998244353
def invmod(a):
    return pow(a,-1,MOD)

N=int(input())                     # (1)数字が1つ 入力例:N

memo = defaultdict(int)
def dp(n):
    # dp(n): nから始めた時のdp(n)がNになる確率
    if (n >= N):
        if n == N:
            return 1
        return 0
    if n in memo.keys():
        return memo[n]
    res = 0
    for ii in range(2,6+1):
        res += dp(n * ii)
    memo[n] = (res * invmod(5)) % MOD
    return memo[n]

ans = dp(1)
print(ans)
