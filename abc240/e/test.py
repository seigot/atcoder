import sys
 
sys.setrecursionlimit(100000000)
 
N = int(input())
connections = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    connections[u].append(v)
    connections[v].append(u)
 
minimum_id = 1
ans = [None for _ in range(N+1)]
 
def dfs(src, dst):
    global minimum_id
    global ans
    left = minimum_id
    right = 0
    for connection in connections[dst]:
        if not connection == src:
            l, r = dfs(dst, connection)
            left = min(left, l)
            right = max(right, r)
    if left == minimum_id:
        minimum_id += 1
        right = left
    ans[dst] = (left, right)
    return left, right
 
dfs(0, 1)
for a in ans[1:]:
    print(*a)
