N=int(input())
AB = []
for _ in range(N):
    A,B=map(int, input().split())
    AB.append((A,B))

# 全探索
ans = 10**10
for ii in range(N):
       for jj in range(N):
            a1 = AB[ii][0]
            a2 = AB[jj][1]
            if ii == jj:
                ans = min(ans, a1+a2)
            else:
                val = max(a1,a2)
                ans = min(ans,val)
print(ans)

