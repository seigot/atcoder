n=int(input())
s=[]
for i in range(n):
    s.append(input())

# 探索用の二次元配列(0埋め)
cnt=[[0 for j in range(10)]for i in range(10)]
#print(cnt)

# 探索
## リール
for i in range(n):
    ## 数値が何番目に来るか並び替える
    for j in range(10):
        cnt[int(s[i][j])][j] = cnt[int(s[i][j])][j]+1

# 各数値の最小を数える
mx=[0 for i in range(10)]
## 各リール
for i in range(10):
    ## cntが1以上の場合 
    for j in range(10):
        mx[i]=max(mx[i], 10 * (cnt[i][j] - 1) + j)

# 一番小さい数値を結果として返す
print(min(mx))

