# bfs
from collections import deque
visited = set()
def bfs(n):
    q = deque()
    q.append(n)
    visited.add(n)
    while q:
        tx = q.popleft()
        for dx in gh[tx]:
            if dx in visited:
                # already visited
                continue
            # not visited
            q.append(dx)
            visited.add(dx)
bfs(N)

# 幅優先探索(2次元座標を座標圧縮して探索する)
# s:始点座標(座標圧縮済)
# n:座標の数(width*height)
# mat:二次元座標
# return: depth
def bfs(s, n, mat, width, height):
    que = deque([s])
    INF = 10**15
    depth = [INF]*(n)
    pre = [-1]*(n)
    depth[s] = 0
    while que:
        crr = que.popleft()
        y, x  = crr//width, crr % width
        for dx, dy in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            nx = x + dx
            ny = y + dy
            if not (0 <= nx < width and 0 <= ny < height):
                continue
            if mat[ny][nx] == "#":
                continue
            nxt = ny*width+nx
            if depth[nxt] == INF:
                depth[nxt] = depth[crr]+1
                pre[nxt] = crr
                que.append(nxt)
    return depth

ds = bfs(s, h*w, a, w, h) # startからのdepth(全座標)
dg = bfs(g, h*w, a, w, h) # goalからのdepth(全座標)

# 幅優先探索
# (gh:グラフ)
# s: 初めの頂点番号
# n: 頂点数
# sから全頂点への距離を求める
# return
#  depth: 距離(list) もし辿り着けない頂点がある場合は-1をいれる
#  pre:   探索前の頂点番号(list)
def bfs(s, n):
    que = deque()
    que.append(s)
    depth = [-1]*(n+1)
    pre = [-1]*(n+1)
    depth[s] = 0
    while que:
        crr = que.popleft()
        for nxt in gh[crr]:
            if depth[nxt] == -1:
                depth[nxt] = depth[crr]+1
                pre[nxt] = crr
                que.append(nxt)
    return depth, pre

d, _ = bfs(1, n+m+1)
