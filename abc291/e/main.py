#!/usr/bin/env python3                                                                          
N,M = map(int,input().split())
XY = []
for ii in range(M):
  x, y = map(int, input().split())
  XY.append((x-1,y-1))
#print(XY)

# トポロジカルソート
# https://ikatakos.com/pot/programming_algorithm/graph_theory/topological_sort
def topo(in_edge,out_node):
  # 流入リンク数が0であるノードのセットS(DAGなら最低1つは存在する) --> 起点となるノード
  S = [i for i, c in enumerate(in_edge) if c == 0]
  # 暫定ソート結果を保持する空リストL
  L = []

  # Sが空になるまでループ
  while S:
      if len(S) > 1:
        print("No")
        exit()
      n = S.pop()
      L.append(n)
      for m in out_node[n]:
          in_edge[m] -= 1
          if in_edge[m] == 0:
              S.append(m)
  return L

in_edge = [0]*N
out_node = [[] for _ in range(N)]
for x,y in XY:
  in_edge[y] += 1       # 入力されるedgeの数を数えておく
  out_node[x].append(y) # 出力先ノードの数を数えておく

# トポロジカルソート
# https://ikatakos.com/pot/programming_algorithm/graph_theory/topological_sort
order = topo(in_edge,out_node)
#print(order)

# orderは値の小さな順のindexが並んでいるので、orderの順に1~Nの値を入力する
ans = [0]*N
count = 1
for i in order:
  ans[i] = count
  count += 1
  
print("Yes")
print(*ans)