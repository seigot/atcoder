import math

N=int(input())
P=list(map(int,input().split()))

bigM= 3*N

class SegmentTree():
    def __init__(self,n,query):
        self.n=n
        self.logM = int(math.log2(n)+0.99)
        self.M = 2 ** self.logM
        init_val = bigM if query == "min" else -bigM
        self.tree = [init_val]*(2*self.M)
        self.startpos = self.M - 1
        self.query = query
    def update(self,ix,x):
        ixw = ix + self.startpos
        self.tree[ixw] = x
        x1 = x
        while ixw > 0:
            ixw //= 2
            if self.query == "min":
                self.tree[ixw] = min(self.tree[ixw*2],self.tree[ixw*2+1])
            else:
                self.tree[ixw] = max(self.tree[ixw*2],self.tree[ixw*2+1])
    def get(self,from_ix,to_ix):
        ixw1 = self.startpos + from_ix
        ixw2 = self.startpos + to_ix
        vals = [self.tree[ixw1],self.tree[ixw2]]
        while ixw1 > 0:
            if ixw1 >= ixw2 - 1:
                break
            if ixw1 %2 == 0:
                vals.append(self.tree[ixw1+1])
            ixw1 //=2
            if ixw2 %2 == 1:
                vals.append(self.tree[ixw2-1])
            ixw2 //=2
        if self.query == "min":
            return min(vals)
        else:
            return max(vals)

answers=""
D=[bigM]*N

tree1 = SegmentTree(N,"max")
tree2 = SegmentTree(N,"min")
tree3 = SegmentTree(N,"min")
tree4 = SegmentTree(N,"max")

A=[0]*N
B=[0]*N

for i in range(N):
    Pi = P[i]
    Ai = P[i]+i
    Bi = P[i]-i

    if i > 0 :
        if Pi > 1:
            dww = tree1.get(1,Pi-1)
            #print(dww,Pi,i,tree1.tree)
            D[i]=min(D[i],Ai - dww)
    tree1.update(Pi,Ai)

for i in range(N):
    Pi = P[i]
    Ai = P[i]+i
    Bi = P[i]-i
    if i> 0:
        if Pi < N:
            dww = tree3.get(Pi+1,N)
            D[i]=min(D[i],dww - Bi)
    tree3.update(Pi,Bi)

for i in range(N):
    iw = N - i - 1
    Piw=P[iw]
    Aiw=P[iw]+iw
    Biw=P[iw]-iw
    if iw < N-1:
        if Piw < N:
            dww = tree2.get(Piw+1,N)
            D[iw]=min(D[iw],dww-Aiw)
    tree2.update(Piw,Aiw)

for i in range(N):
    iw = N - i - 1
    Piw=P[iw]
    Aiw=P[iw]+iw
    Biw=P[iw]-iw
    if iw < N-1:
        if Piw > 1:
            dww = tree4.get(1,Piw-1)
            dw4=Biw - dww
            D[iw]=min(D[iw],Biw-dww)
    tree4.update(Piw,Biw)

print(*D)

