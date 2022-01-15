# https://atcoder.jp/contests/abc235/submissions/28570393

class UnionFind():
    def __init__(self,n):
        self.n = n
        self.parents = [-1] * n
    
    def find(self,x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
 
    def issame(self,x,y):
        return self.find(x) == self.find(y)
    
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.parents[x] > self.parents[y]:
            x,y = y,x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return True
    
    def size(self,x):
        return -self.parents[self.find(x)]
 
N, M, Q = map(int,input().split())
G = [[] for _ in range(N)]
abc = []
for _ in range(M):
    ai,bi,ci = map(int,input().split())
    abc.append((ci,ai,bi))
abc.sort()
mint = []
uf = UnionFind(N+1)
for ci,ai,bi in abc:
    if uf.issame(ai,bi):
        continue
    mint.append((ci,ai,bi))
    uf.union(ai,bi)
    if uf.size(ai) == N:
        break
 
uvw = []
for i in range(Q):
    ui,vi,wi = map(int,input().split())
    uvw.append((wi,ui,vi,i))

uvw.sort()
ans = [False]*Q
uf = UnionFind(N+1)
cid = 0
ci,ai,bi = mint[cid]
for wi,ui,vi,idx in uvw:
    while ci < wi:
        uf.union(ai,bi)
        cid += 1
        if cid >= N-1:
            break
        ci,ai,bi = mint[cid]

    if uf.issame(ui,vi):
        ans[idx] = False
    else:
        ans[idx] = True
 
for ai in ans:
    if ai:
        print('Yes')
    else:
        print('No')
