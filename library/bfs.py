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
        y, x  = crr//w, crr % w
        for dx, dy in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            nx = x + dx
            ny = y + dy
            if not (0 <= nx < width and 0 <= ny < height):
                continue
            if mat[ny][nx] == "#":
                continue
            nxt = ny*w+nx
            if depth[nxt] == INF:
                depth[nxt] = depth[crr]+1
                pre[nxt] = crr
                que.append(nxt)
    return depth

ds = bfs(s, h*w, a, w, h) # startからのdepth(全座標)
dg = bfs(g, h*w, a, w, h) # goalからのdepth(全座標)
