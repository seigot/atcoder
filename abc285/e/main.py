n = int(input())
a = [0] + list(map(int,input().split()))

# 最後の休日がi日目である時の生産量のMAX
dp = [0 for i in range(n)]

pre = a[::1]
for i in range(1,n+1):
  pre[i] += pre[i-1]


for i in range(1, n):
  for j in range(i):
    len = i-j-1
    tmp = 2*pre[len//2]
    if len % 2 == 1:
      tmp += a[len//2+1]
    dp[i] = max(dp[i], dp[j] + tmp)
  
ans = 2*pre[(n-1)//2]
if (n-1) % 2 == 1:
  ans += a[(n-1)//2+1]
for i in range(1,n):
  ans = max(dp[i] + dp[n-i], ans)

print(ans)

