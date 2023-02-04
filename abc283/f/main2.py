from collections import defaultdict, deque, Counter
from heapq import heappop, heappush
from bisect import bisect_left, bisect_right
from math import gcd

n = int(input())
p = list(map(int,input().split()))
INF = 10**8
seg_len = 1<<18 # > 5*(10**5)
seg = [-INF]*(2*seg_len)

# 必要に応じて初期状態構築

def update(pos,x):
  pos += seg_len
  seg[pos] = x 
  while True: 
    pos >>= 1 
    if not pos: break 
    seg[pos] = max(seg[pos<<1],  seg[pos<<1|1])

def get_query(l,r):
  l += seg_len; r += seg_len
  res = -INF
  while l < r: 
    if l & 1: 
      res = max(res, seg[l] )
      l += 1 
    if r & 1: 
      r -= 1 
      res = max(res , seg[r] )
    l >>= 1; r >>= 1
  return res

ans = [INF]*n


for i in range(n):
  if i != 0:
    tmp = get_query(0, p[i])
    ans[i] = p[i] + i - tmp
  update(p[i], p[i]+i)

seg = [-INF]*(2*seg_len)
for i in range(n):
  if i != 0:
    tmp = get_query(p[i]+1, seg_len-10)
    ans[i] = min(ans[i], -p[i] + i - tmp)
  update(p[i], -p[i]+i)

seg = [-INF]*(2*seg_len)
for i in range(n)[::-1]:
  if i != n-1:
    tmp = get_query(0, p[i])
    ans[i] = min(ans[i], p[i] - i - tmp)
  update(p[i], p[i]-i)
  

seg = [-INF]*(2*seg_len)
for i in range(n)[::-1]:
  if i != n-1:
    tmp = get_query(p[i]+ 1, seg_len-10)
    ans[i] = min(ans[i], -p[i] - i - tmp)
  update(p[i], -p[i]-i)

print(*ans)


