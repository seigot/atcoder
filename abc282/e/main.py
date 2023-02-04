#!/usr/bin/env python3

n,m = map(int,input().split())
a = list(map(int,input().split()))
graph = []
for i in range(n-1):
  for j in range(i+1, n):
    tmp = pow(a[i],a[j],m)+pow(a[j],a[i],m)
    graph.append([i,j,tmp%m])

#union find
p = [-1]*(n+1)
def find(x):
  if p[x] < 0:
    return x
  else:
    p[x] = find(p[x])
    return p[x]
def union(x,y):
  x = find(x)
  y = find(y)
  if x == y:
    return
  if p[x] > p[y]:
    x,y = y,x
  p[x] += p[y]
  p[y] = x

# コスト降順に探索する（コストが大きいものから順番に）
graph.sort(key = lambda x:-x[2]) #コストを示すindexに注意
ans = 0
for i in range(len(graph)):
  a,b,c = graph[i]
  if find(a) != find(b):
    # union find
    # 同じ木に属していなければコストを足して同じ木にする
    ans += c
    union(a,b)

print(ans)