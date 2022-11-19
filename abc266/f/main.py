import sys
from collections import defaultdict, deque
sys.setrecursionlimit(5*10**5)
input = sys.stdin.readline
#import pypyjit
#pypyjit.set_param('max_unroll_recursion=-1')

n = int(input())
graph = [[] for i in range(n+1)]
for i in range(n):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
q = int(input())
qs = [list(map(int,input().split())) for i in range(q)]

out = None
from collections import deque

# N 頂点 N 辺の連結な単純無向グラフ G
#  -- ちょうど一つの閉路及びその閉路上の頂点を根とする木とみることができる
#   -- 閉路上の頂点を探索する
#   -- 閉路上の頂点を根としたときに、

# 閉路上の頂点を探索する
# 幅優先探索により、queに探索順番を入れる（頂点1から始まる）
que = deque([(1,-1)]) #(cur, pre)
depth = [-1]*(n+1)
depth[1] = 0
while que:
    if out: break
    crr,pre = que.popleft()
    for nxt in graph[crr]:
        if depth[nxt] == -1:
            # 未探索の場合
            depth[nxt] = depth[crr]+1
            que.append((nxt, crr))
        elif nxt != pre:
            # 探索済みであり、かつ1つ前ではない場合、これは閉路上の頂点である
            out = [crr, nxt]

# 閉路上の頂点（out[0]）を根とみたときに深さとつながりを求める、幅優先探索で求める
que = deque([out[0]])
depth = [-1]*(n+1)
prev = [-1]*(n+1)
depth[out[0]] = 0
while que:
    crr = que.popleft()
    for nxt in graph[crr]:
        if [crr,nxt] == out: continue
        if depth[nxt] == -1:           # 未探索である場合
            prev[nxt] = crr            # 親子関係
            depth[nxt] = depth[crr]+1  # 深さ
            que.append(nxt)            # 次の探索用

# 閉路上の前を基準に順番に入れなおす、親をみていく
ans = []     # ここには閉路上の点が含まれる、全ての頂点を含む
             # out[1]の点はprevが-1になる。これが一番最後にはいる
now = out[1] # 閉路上の点
while now != -1:
    ans.append(now)
    now = prev[now]

# 閉路上の点に着目する
ans = set(ans)
d = defaultdict(int)
for i in ans:
    ss = set()
    que = deque([i])
    # 閉路上の点を幅優先探索する
    while que:
        crr = que.popleft()
        ss.add(crr)
        d[crr] = i   # 探索箇所の根はiであるということを覚えさせる
        for nxt in graph[crr]:
            # crrに繋がっている点が未探索であれば探索する
            if nxt in ss or nxt in ans: continue
            que.append(nxt)

for x,y in qs:
    if d[x] == d[y]:
        print('Yes')
    else:
        print('No')



