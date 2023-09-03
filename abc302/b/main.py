#!/usr/bin/env python3                                                                          
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
H,W=map(int, input().split())
maze = [list(input()) for h in range(H)] # maze(###.###) のようなスペースなしの2次元配列で受け取り

snuke="snuke"
for jj in range(H):
    for ii in range(W):
        for pos in dpos8:
            for cnt in range(len(snuke)):
                tx = ii + pos[0]*cnt
                ty = jj + pos[1]*cnt
                if tx < 0 or W <= tx or ty < 0 or H <= ty:
                    break
                if maze[ty][tx] != snuke[cnt]:
                    break
                if cnt == 4:
                    # answer
                    for kk in range(len(snuke)):
                        print(jj+pos[1]*kk+1, ii+pos[0]*kk+1)
                    exit()
