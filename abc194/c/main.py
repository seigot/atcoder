from collections import Counter
N=int(input())
A=list(map(int, input().split()))

# 各数字の出現回数をカウント
cnt = Counter(A)

ans = 0
for x in range(-200, 201):
    for y in range(-200, 201):
        # 数字の組み合わせと、出現回数を計算
        ans += (x - y)**2 * (cnt[x] * cnt[y])
print(ans//2)
