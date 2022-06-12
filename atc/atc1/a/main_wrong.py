import sys
sys.setrecursionlimit(10**7) # 再起回数の設定

H, W = map(int, input().split())
maze = [list(input()) for h in range(H)]
#print(maze)
for h in range(H):
    for w in range(W):
        if maze[h][w] == "s":
            sx, sy = h, w
nyy = [0, 0, -1, 1]
nxx = [-1, 1, 0, 0]
# 深さ優先探索
def dfs(x, y):
    # 範囲外や壁の場合は終了
    if y >= W or y < 0 or x >= H or x < 0 or maze[x][y] == '#':
       return

    # ゴールに辿り着ければ終了
    if maze[x][y] == 'g':
        print('Yes')
        exit()

    maze[x][y] = '#' # 確認したルートは壁にしておく

    # 上下左右への移動パターンで再起していく
    for ii in range(4):
        ny = min(W-1, max(0, y + nyy[ii]))
        nx = min(H-1, max(0, x + nxx[ii]))
        if ny >= W or ny < 0 or nx >= H or nx < 0 or maze[nx][ny] == '#':
           continue
        dfs(nx, ny)
    #dfs(x-1, y)
    #dfs(x+1, y)
    #dfs(x, y-1)
    #dfs(x, y+1)

dfs(sx, sy) # スタート位置から深さ優先探索
print('No')