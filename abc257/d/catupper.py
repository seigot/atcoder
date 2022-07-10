N = int(input())
jumps = [
    tuple(map(int, input().split()))
    for _ in range(N)
]

def ok(S):
    reachable = [[False] * N for _ in range(N)]
    for i in range(N):
        p = jumps[i][2]
        for j in range(N):
            d = abs(jumps[i][0] - jumps[j][0]) + abs(jumps[i][1] - jumps[j][1])            
            reachable[i][j] = d <= S*p

    for i in range(N):
        for j in range(N):
            for k in range(N):
                reachable[j][k] |= reachable[j][i] and reachable[i][k]

    for i in range(N):
        if all(reachable[i]):
            return True
    return False


bottom, top = 0, 4 * 10 ** 9

while top - bottom > 1:
    mid = (top + bottom) // 2
    if ok(mid):
        top = mid
    else:
        bottom = mid

print(top)
