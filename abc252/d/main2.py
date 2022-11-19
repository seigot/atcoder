N=int(input()) # 文字列の長さ
A=list(map(int,input().split())) # A_N

UPPER=2*10**5

cnt=[0]*(UPPER+1)

# cnt[i] = Aに含まれる i 以下の値の個数
# cnt[i] = |{ j | A[j]<=i }|

## Aに含まれるAiの数を数える
for i in range(N):
  cnt[A[i]]+=1

## Aに含まれるi以下の値の個数を数えていく
for i in range(UPPER):
  cnt[i+1]+=cnt[i]

ans=0
# jを全探索して個数を数える
for j in range(N):
  # とあるjを選択した際に、
  #  A[j]より小さい数の個数 * A[j]より大きい数の個数　として求められる
  ans+=cnt[A[j]-1]*(N-cnt[A[j]])

print(ans)

