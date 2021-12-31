# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
#input_line = input()
#print("XXXXXX")

#H, W = map(int, input().split())
#
#STR=["a"] * H
#for i in range(H):
#    STR[i]=str(input())
#
#print(STR)

import sys
sys.setrecursionlimit(10**7) # 再起回数の設定

H, W = map(int, input().split())
maze = [list(input()) for h in range(H)]

for h in range(H):
    for w in range(W):
        if maze[h][w] == "S":
            sx, sy = h, w


# 深さ優先探索
def dfs(x, y):
    # 範囲外や壁の場合は終了
    if y >= W or y < 0 or x >= H or x < 0 or maze[x][y] == '#':
        return

    # ゴールに辿り着ければ終了
    #if maze[x][y] == 'G':
    if x == 0 or x == W-1 or y == 0 or y == H-1:
        print('YES')
        exit()

    maze[x][y] = '#' # 確認したルートは壁にしておく

    # 上下左右への移動パターンで再起していく
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)

dfs(sx, sy) # スタート位置から深さ優先探索
print('NO')

