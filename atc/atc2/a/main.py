import collections

R,C=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
sy,sx=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
gy,gx=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B

# 座標を(0,0)基準にする
sy -= 1
sx -= 1
gy -= 1
gx -= 1

# input
c = []
for ii in range(R):
    l = input()
    c.append(l)
#print(c)
dist=[[-1 for j in range(C)] for i in range(R)]
visitedtbl=[[-1 for j in range(C)] for i in range(R)]
#print(dist)
currentq = collections.deque()
currentq.append((0,sy,sx))
# 探索
d = 0
diff_y = [-1, 1, 0,  0]
diff_x = [0,  0, -1, 1]

while True:

    d, ty, tx = currentq.popleft()

    # 訪れていなければ更新
    dist[ty][tx] = d

    # goalに到達したらbreak
    #if ty == gy and tx == gx:
    #    break

    # 探索継続、上下左右を探索できるかチェック
    for ii in range(4):
        ny = min(R-1, max(0, ty + diff_y[ii]))
        nx = min(C-1, max(0, tx + diff_x[ii]))
        if c[ny][nx] == '.' and visitedtbl[ny][nx] == -1:
            # 未探索であれば対象に追加
            currentq.append((d+1,ny,nx))
            visitedtbl[ny][nx] = 0
            #dist[ny][nx] = d+1

    if len(currentq) <= 0:
        # queueがなくなったら探索終了
        break

print(dist[gy][gx])




