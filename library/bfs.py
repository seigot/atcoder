# bfs
visited = set()
def bfs(n):
    q = deque()
    q.append(n)
    visited.add(n)
    while q:
        tx = q.popleft()
        for dx in gh[tx]:
            if dx in visited:
                # already visited
                continue
            # not visited
            q.append(dx)
            visited.add(dx)
bfs(N)
