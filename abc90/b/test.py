A, B = map(int,input().split())

# 5桁の回文を全て求める
l = []
for i in range(10000, 100000):
    ll = list(str(i))
    if ll[::] == ll[::-1]:
        l.append(i)

# A, Bの区間内に入っているかどうかを調べる
ans=0
for i in l:
    if int(i) >= A and int(i) <= B:
        ans += 1

print(ans)
