# 木がある。次数がdiを超えないように辺を選ぶと、重みの総和の最大値はどうなるだろうか
import heapq
import sys
from collections import deque
sys.setrecursionlimit(500000)
N = int(input())
D = [int(hoge) for hoge in input().split()]
NextList = [set() for _ in range(N)]
Edges = dict()
for _ in range(N-1):
    u, v, w = [int(hoge) for hoge in input().split()]
    if w < 0:
        # 0は結局使わないので重み0にしておく
        w = 0
    NextList[u-1].add(v-1)
    NextList[v-1].add(u-1)
    Edges[(u-1, v-1)] = w
    Edges[(v-1, u-1)] = w

# 仮に、根を頂点0とする。
parent = [-1] * N
BFS = deque([0])
# 各頂点の親を求める
while BFS:
    curpos = BFS.pop()
    for togo in NextList[curpos]:
        # 子供候補の一覧を取得する
        if togo != 0 and parent[togo] == -1:
            # 根ではなく、親が未探索である場合
            parent[togo] = curpos
            BFS.appendleft(togo)

# 頂点ごとに、「自分の親に辺を供給する余地がある」「ない」の2種類で最大重みを出力する
# Costsはdp[N][N]のようなリスト
Costs = [[-1, -1] for _ in range(N)]

def calc_cost(curpos):
    # (0ではない場合であり、かつ)子がなければスキップする
    if len(NextList[curpos]) == 1 and curpos != 0:
        return(0, 0)
    else:
        children_cost = []
        for child in NextList[curpos]:
            if child != parent[curpos]:
                yoryokuNG, yoryokuOK = calc_cost(child)
                if D[child] != 0:
                    children_cost.append(
                        (
                            yoryokuNG,
                            max(yoryokuNG, yoryokuOK + Edges[(curpos, child)])
                        )
                    )
                else:
                    children_cost.append(
                        (yoryokuNG, yoryokuNG)
                    )
                # [選ばないコスト,選ぶコスト]
        # dが0だったらgrowthはゼロに
        growth = []
        for i, j in children_cost:
            heapq.heappush(growth, i-j)
        base = sum([i for i, j in children_cost])
        # 0本だった場合, ans0,ans1 ともにbaseをかえす
        if D[curpos] == 0:
            return (base, base)
        for i in range(len(growth)):
            # 余力ありの場合
            g = heapq.heappop(growth)
            if i+1 == D[curpos]:
                return(base - g, base)
            base -= g
        return(base, base)


print(max(calc_cost(0)))

