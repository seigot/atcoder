import collections
n, x=map(int,input().split())
l = collections.defaultdict(list)
ans=set()
ans.add(0)
l[0].append(ans)

# Nstep分繰り返す
for i in range(n):
    a, b=map(int,input().split())
    # N=1,2,3...毎に集合を更新する。set()を使う事で重複問題を解決する。
    cnt=set()
    ll = l[i][0]
    for j in ll:
        cnt.add(j + a)
        cnt.add(j + b)
    l[i+1].append(list(cnt))
if x in l[n][0]:
    print("Yes")
else:
    print('No')
