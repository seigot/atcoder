from heapq import heappush,heappop

class DeletablePQ:
  def __init__(self,data=None,greater=False):
    self.greater=greater
    self.count= {}
    self.que=[]
    if data:
        for x in data:
            heappush(self.que,x*(-1 if greater else 1))
            if self.count.get(x): self.count[x] += 1
            else: self.count[x] = 1
    self.len = len(self.que)

  def push(self,x):
    heappush(self.que,x*(-1 if self.greater else 1))
    if self.count.get(x): self.count[x] += 1
    else: self.count[x] = 1
    self.len += 1
    
  def remove(self,x):
    self.count[x] -= 1
    self.len -= 1
  
  def nremove(self,x,num=1):
    self.count[x] -= num
    self.len -= num
    if self.count[x] < 0:
      self.len -= self.count[x]
      self.count[x] = 0
    
  def pop(self):
    x,self.count[x]=-1,0
    while self.count[x]<1: x=heappop(self.que)*(-1 if self.greater else 1)
    self.len -= 1
    self.count[x] -= 1
    return x
  
  def count(self,x):
    return self.count[x] if self.count[x]>0 else 0
  
  def get_val(self):
    while self.count.get(self.que[0]*(-1 if self.greater else 1)) != None and self.count[self.que[0]*(-1 if self.greater else 1)]<1:
        heappop(self.que)
    return self.que[0]*(-1 if self.greater else 1)

  def merge(self, other):
        while len(other) > 0: self.push(other.pop())
  
  def __len__(self):
    return self.len

# https://atcoder.jp/contests/abc212/submissions/24661232
Q=int(input())
que = DeletablePQ()
base = 0
for _ in range(Q):
  *q,=map(int,input().split())
  if q[0] == 1:
    que.push(q[1]-base)
  elif q[0] == 2:
    base += q[1]
  else:
    res = que.get_val()
    que.remove(res)
    print(res+base)
