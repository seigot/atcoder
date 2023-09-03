L,N,M = map(int,input().split())

list1 = []
#index1 = [-1]*L
s1 = set()
list2 = []
#index2 = [-1]*L
s2 = set()
s12 = set()

now = 0
for i in range(N):
    v,l = map(int,input().split())
    list1.append([v, now+l])
    s1.add(now+l)
    now += l
now = 0
for i in range(M):
    v,l = map(int,input().split())
    list2.append([v, now+l])
    s2.add(now+l)
    now += l
s12 = s1.union(s2)
s12.add(0)
idx1 = 0
idx2 = 0
ans = 0
sorted_s12 = sorted(list(s12))
# 高々2N個
for ii in range(len(sorted_s12)-1):
    c_idx = sorted_s12[ii]
    next_idx = sorted_s12[ii+1]
    x = list1[idx1][0]
    y = list2[idx2][0]
    # 値をアップデート
    if x == y:
        ans += next_idx - c_idx
    # idxの更新、値のアップデートの区切りに相当する場合
    if next_idx in s1:
        idx1 += 1
    if next_idx in s2:
        idx2 += 1

print(ans)


