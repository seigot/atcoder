# bit[]に値をいれる
def add(bit, pos, val):
    pos += 1  # 1-index
    while pos < len(bit):
        bit[pos] += val
        pos += pos & -pos
# bit[]の値を取得する
def get(bit, pos):
    pos += 1  # 1-index
    ans = 0
    while pos > 0:
        ans += bit[pos]
        pos -= pos & -pos
    return ans

N = int(input())
C = list(map(int, input().split()))
X = list(map(int, input().split()))

# colors
colors = {}
for i in range(N):
    c = C[i]
    x = X[i]
    if c not in colors:
        colors[c] = []
    colors[c].append(x)

cost = 0

bit = [0] * (N+10)

for i in range(N-1, -1, -1):
    x = X[i]
    cost += get(bit, x-1) # コストを全て足す
    add(bit, x, 1)        # 

# 同じ色同士が数えられているので戻す
for i in range(N-1, -1, -1):
    x = X[i]
    add(bit, x, -1)

for c in colors:
    xs = colors[c]
    for x in xs[::-1]:
        cost -= get(bit, x-1)
        add(bit, x, 1)

    for x in xs[::-1]:
        add(bit, x, -1)

print(cost)
        
