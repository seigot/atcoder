n=int(input())
res=0
t=9
mod=998244353

while n>t:
    # 対象の桁の合計値を求める
    res+=(t*(t+1))//2
    res%=mod
    # 対象の桁の合計値は求めたので差分
    n-=t
    # 次の桁
    t*=10
# 一番上の桁の合計値を求める
res+=(n*(n+1))//2

res%=mod
print(res)
