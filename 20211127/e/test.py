#n, m = map(int, input().split())
#l = [list(map(int, input().split())) for l in range(m)]

#print(n, m, l)

from collections import defaultdict
 
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
 
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
 
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
 
        if x == y:
            return
 
        if self.parents[x] > self.parents[y]:
            x, y = y, x
 
        self.parents[x] += self.parents[y]
        self.parents[y] = x
 
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
 
    def group_count(self):
        return len(self.roots())
 
N, M = map(int, input().split())
nodes = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    nodes[a-1].append(b-1)
 
uf = UnionFind(N)
ans = [0]            # 0個
#print(nodes)
#print("--")
nodes = nodes[1:]    # nodesの1つめ以降を取得する(1つめをなくすと頂点数は0になるため)
#print(nodes)
nodes = nodes[::-1]  # reverse
#print("--")
#print(nodes)
#print("--")
g = 0 #グループ数
for i, edges in enumerate(nodes): #reverseしたリストを順番に探索していく
    #print(i), 0,1,2,3,4
    #頂点が増えた分グループを追加
    g += 1
    #繋がるグループ数
    s = set()              # 集合
    for e in edges:        # 頂点を探す
        s.add(uf.find(e))  # 各頂点の親のうち重複しないものの数を数える
    m = len(s)             # 繋がるグループの数
    for e in edges:
        uf.union(e, N-i-1) # 連結させる（注目しているのはi番目=元々のN-(i+1)番目に相当する）
    #現在のグループ数から新規につながった分を引く
    g -= m                 # 例えば1つ頂点が増えても1グループと繋がったら増えたグループは0個
    ans.append(g)          # グループの数を格納する
 
ans = ans[::-1]
for a in ans:
    print(a)
