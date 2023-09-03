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

## ---
# 深さ幅優先探索
# 再帰で実装する
# usedフラグ(True:使用した, False:使用していない)を渡すDFS
# used = [False] * N
def dfs(used):
    if all(used):
        return 0
    # Falseのものから1つ選択する
    v = used.index(False)
    used[v] = True
    ret = 0
#    for w in range(v + 1, N):
    for w in range(N):
        # Falseの残り１つのものからもう1つ選択する
        if not used[w]:
            used[w] = True
            val = D[v][w] + dfs(used)
            ret = max(ret, val)
            used[w] = False
    used[v] = False
    return ret
used = [False] * N
ans = 0
if N % 2 == 0:
    ans = dfs(used)
else:
    for v in range(N):
        used[v] = True
        ans = max(ans, dfs(used))
        used[v] = False
print(ans)
