# 長さ N の数列 A=(A1,A2,…,AN) が与えられます。
# 以下の 2 条件をともに満たすような整数の組 (i,j,k) の個数を求めてください。
# 1≤i<j<k≤N
# Ai ,Aj ,Ak は相異なる

n = int(input())
from collections import defaultdict
a = list(map(int,input().split()))
d = defaultdict(int)
for i in range(n):
  d[a[i]] += 1

# NC3 - sigma (NC2) - sigma NC3
ans = n*(n-1)*(n-2)//6

#print(d.items())
#print(d.keys())
#print(d.values())
# sigma (NC2)
# sigma NC3
for k,v in d.items():
  if v >= 2:
    # 2つ以上選択することがある
    # nC2 * (他の(n-v)種類の数)
    ans -= (n-v)*v*(v-1)//2
  if v >= 3:
    # 3つ以上選択することがある
    ans -= v*(v-1)*(v-2)//6
print(ans)
