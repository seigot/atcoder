n = int(input())
a = list(map(int,input().split()))
INF = 10**18
c = [[INF]*n for i in range(n)]
for i in range(n):
  s = input()
  for j in range(n):
    if s[j] == "Y":
      c[i][j] = 1

#ワーシャルフロイド法:c[i][j]:iからjまでの距離、二次元配列
def wf(n):
  for k in range(n):
    for i in range(n):
      for j in range(n):
        c[i][j] = min(c[i][j],c[i][k]+c[k][j])

wf(n)
ss = [[0]*n for i in range(n)]
for i in range(n):
  for j in range(n):
    if c[i][j] == 1:
      ss[i][j] = a[i] + a[j]



for k in range(n):
  for i in range(n):
    for j in range(n):
      if c[i][k] + c[k][j] == c[i][j]:
        ss[i][j] = max(ss[i][j],ss[i][k]+ss[k][j] - a[k])
      

q = int(input())
for i in range(q):
  u,v = map(int,input().split())
  u -= 1
  v -= 1
  if c[u][v] == INF:
    print("Impossible")
  else:
    print(c[u][v], ss[u][v])