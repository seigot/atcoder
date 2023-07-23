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

# 幅優先探索（方向に状態をもつ）
dy = [1,-1,0,0]
dx = [0,0,1,-1]
def bfs(s, st):
    que = deque([(s,st)])
    # 状態を持ったまま幅優先探索する
    # 上下左右通過した方向に状態を持たせる
    depth = [[-1]*5 for i in range(n*m)]
    depth[s][st] = 0
    while que:
        crr,state = que.popleft()
        x,y = crr//m, crr%m
        if state == 4:
            # 4方向に移動できる状態
            for i in range(4):
                nx,ny = x + dx[i], y + dy[i]
                nxt = nx*m+ny
                if (nx < 0 or n <= nx or ny < 0 or m <= ny):
                    # エリア外であればskip
                    continue
                if S[nx][ny] != "#" and depth[nxt][i] == -1:
                    # 岩ではなく未探索である場合は探索実施
                    depth[nxt][i] = 1#depth[crr][state]+1
                    que.append((nxt, i))
        else:
            # 1方向にのみ移動できる状態
            # state=0~3 (dx,dyに対応する)
            nx,ny = x + dx[state], y + dy[state]
            nxt = nx*m+ny
            if (nx < 0 or n <= nx or ny < 0 or m <= ny):
                # エリア外であればskip
                continue
            if S[nx][ny] == "#": #and depth[crr][4] == -1:
                # 岩の場合は4方向に探索
                depth[crr][4] = 1#depth[crr][state] + 1
                que.append((crr, 4))
            elif S[nx][ny] != "#" and depth[nxt][state] == -1:
                # 岩ではなく未探索である場合は探索実施
                depth[nxt][state] = 1#depth[crr][state] + 1
                que.append((nxt, state))
    return depth

d = bfs(m+1,4)
ans = 0
for i in range(n):
    for j in range(m):
        # 一度でも通過した事がある場合は+1
        ans += sum(d[i*m+j]) != -5
print(ans)
