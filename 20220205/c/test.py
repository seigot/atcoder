n=int(input())
res=0
t=9
mod=998244353

KETA=len(str(n))

#while n>t:
for i in range(KETA-1):
    # 対象の桁の合計値を求める
    res+=(t*(t+1))//2
    res%=mod
    # 次の桁
    t*=10

# 一番上の桁の合計値を求める
n = n - ((10**(KETA-1))-1)
res+=(n*(n+1))//2

res%=mod
print(res)
