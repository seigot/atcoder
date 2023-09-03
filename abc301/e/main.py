from math import gcd
from bisect import bisect_left, bisect_right
from heapq import heappop, heappush
from collections import defaultdict, deque, Counter
import sys
input = sys.stdin.readline
# n <= 1<<60 以下くらい

# https://atcoder.jp/contests/abc301/submissions/41386427

def popcnt(n):
    # popcount
    # 2進数の数のうち、"1"の数を高速に数える
    # https://zenn.dev/kiwamachan/articles/ad17cc11f4ad55
    c = (n & 0x5555555555555555) + ((n >> 1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
    c = (c & 0x0f0f0f0f0f0f0f0f) + ((c >> 4) & 0x0f0f0f0f0f0f0f0f)
    c = (c & 0x00ff00ff00ff00ff) + ((c >> 8) & 0x00ff00ff00ff00ff)
    c = (c & 0x0000ffff0000ffff) + ((c >> 16) & 0x0000ffff0000ffff)
    c = (c & 0x00000000ffffffff) + ((c >> 32) & 0x00000000ffffffff)
    return c


h, w, t = map(int, input().split())
a = [input().rstrip() for i in range(h)]
pos = [] # okashi position
s = -1
g = -1

# get start/goal/okashi zahyo
for i in range(h):
    for j in range(w):
        if a[i][j] == "S": # start
            s = i*w+j
        elif a[i][j] == "G": # goal
            g = i*w+j
        elif a[i][j] == "o": # okashi (Max18個は、明らかにbitDPして下さいという事を示唆している)
            pos.append(i*w+j)


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
dpos = [bfs(i, h*w, a, w, h) for i in pos] # 各頂点からのdepth(全座標)
INF = 10**15
n = len(pos) # okashi positionの数

# dp[s][v]: すでに訪れた頂点集合が s であり、最後に訪れた頂点が v であるような状態に至るまでの最短時間
dp = [[INF]*(n) for i in range(1 << n)]
# 初期化
for i in range(n):
    dp[1<<i][i] = ds[pos[i]]

# okashi positionの数だけdpを回す
for bit in range(1 << n):   # bit全探索
    for last in range(n):   # bit全探索対象のうち、"1"が立っているbit(すなわち配る前の座標)について着目する
        if (bit >> last) & 1 == 0: # 該当のbitが立っていない場合はskip
            continue
        for now in range(n):       # 該当のbitが立っている場合は更新
            dp[bit|(1<<now)][now] = min(
                dp[bit|(1<<now)][now], 
                dp[bit][last] + dpos[last][pos[now]]  # 該当のbit --> nowに遷移した場合のコストのうち小さい方を残す
            )

if ds[g] <= t:
    # 初期値0(どの頂点も経由できない)
    ans = 0
else:
    # start - goalまでの距離がtより大きい場合は不可能
    ans = -1
    print(ans)
    exit()
# 全探索
for i in range(1 << n):   # 遷移元
    for last in range(n): # 現在の位置
        d = dp[i][last] + dg[pos[last]] # 現在の位置を経由してgoalへ向かう際のコスト
        if d <= t:
            # 2進数の"1"の数を数える
            ans =  max(ans, popcnt(i))

print(ans)