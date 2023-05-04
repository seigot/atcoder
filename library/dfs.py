# 深さ幅優先探索
# queueとvisitedのadd/discardを組み合わせて実装する
from collections import deque
visited = set()
def dfs(n):
    num = 1
    q = deque()
    q.appendleft(~n)
    q.appendleft(n)
    while q:
        # visitedへ追加
        tx = q.popleft()
        visited.add(tx)
        if tx >= 0:
            for dx in gh[tx]:
                if dx in visited:
                    # already visited
                    continue
                # not visited
                q.appendleft(~dx)
                q.appendleft(dx)
                num += 1
                if num >= 10**6:
                    print(num)
                    exit()
        else:
            # visitedから削除
            tx = ~tx
            visited.discard(tx)
    return num
# 全頂点で探索
ans = dfs(1)

## ---
# 深さ幅優先探索
# 再帰で実装する
l = []
visited = set()
def dfs(n, _visited):
    l.append(n)
    _visited.add(n)
    for dx in gh[n]:
        if dx not in _visited:
            dfs(dx, _visited)
            l.append(n)
# 全頂点で探索
dfs(1,visited)
print(*l)
