from heapq import heappush,heappop

N,K = map(int,input().split())
*A,=map(int,input().split())

done = {0}
q = [0]
ans = []
# 最小値のみに着目する
while len(ans) <= K:
  # 最小値を取り出す
  v = heappop(q)
  ans.append(v)
  for a in A:
    # 最小値とAを足す　
    if v+a not in done:
      heappush(q,v+a)
      done.add(v+a)
      
print(ans[-1])