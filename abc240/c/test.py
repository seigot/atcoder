n, x=map(int,input().split())
ans=set()
ans.add(0)

# Nstep分繰り返す
for i in range(n):
    a, b=map(int,input().split())
    # N=1,2,3...毎に集合を更新する。set()を使う事で重複問題を解決する。
    cnt=set()
    for j in ans:
        cnt.add(j + a)
        cnt.add(j + b)
    ans=cnt
if x in ans:
    print("Yes")
else:
    print('No')
