N,M = map(int,input().split())
G=[[] for _ in range(N)]
for _ in range(M):
  a,b = map(int,input().split())
  a -= 1
  b -= 1
  G[a].append(b)
  G[b].append(a)
  
INF = 10**10
  
def bfs(s):
  d = [INF]*N
  d[s] = 0
  q = [s]
  for v in q:
    for v2 in G[v]:
      if d[v2] < INF:
        continue
      d[v2] = d[v] + 1
      q.append(v2)
  return d

K = int(input())
pd = []
for _ in range(K):
  p,d = map(int,input().split())
  p -= 1
  pd.append((p,d))
  
done = [0]*K
ans = []
# 各頂点は白(0)とすべきか黒(1)とすべきかを決める
for v in range(N):
  D = bfs(v)
  ok = 1
  just = []
  for i,(p,d) in enumerate(pd):
    # 頂点vから頂点pまでの距離がd未満の場合は、頂点vは白(0)にする
    if D[p] < d:
      ok = 0
      break
    # 頂点vから頂点pまでの距離がdの場合は、頂点vは黒(1)にする
    if D[p] == d:
      just.append(i)
  if ok:
    # どの条件からもd未満な頂点ではなく、かつ丁度距離dである場合は黒対象にすべき
    for i in just:
      done[i] = 1
  ans.append(ok)
      
if sum(done) != K:
  # 黒にすべき頂点がKに満たない場合は足りないので"No"
  print("No")
  exit()
  
print("Yes")
print("".join(map(str,ans)))