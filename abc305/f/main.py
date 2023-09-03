# https://atcoder.jp/contests/abc305/submissions/42151175
from collections import defaultdict
from collections import defaultdict, deque, Counter

N, M = map(int, input().split())

G = defaultdict(list)
A = list(map(int, input().split()))[1:]
if N in A:
    print(N)
    OK = input()
    exit()
G[1] = A

# dfs
visited = set([1])
st = [(a, 1) for a in A] # (頂点番号,親)と距離を格納
dq = deque(st)
while True:
    node, par = dq.popleft()
    if node >= 1:
        visited.add(node)
        # 探索対象の頂点から探索実施
        print(node, flush=True)
        X = list(map(int, input().split()))
        G[node] = X[1:]
        # 回答を発見したら探索終了
        if N in G[node]:
            print(N)
            OK = input()
            exit()
        # 探索継続
#        st.append((~node, par))
        dq.appendleft((~node, par)) # (頂点番号,親)の目印を格納
        for nxt in G[node]:
            if nxt in visited:
                # 探索済みの場合はスキップ
                continue
#            st.append((nxt, node))
            dq.appendleft((nxt, node))
    else:
        node = ~node
        # 親ノードを探索
        print(par, flush=True)
        X = list(map(int, input().split()))
