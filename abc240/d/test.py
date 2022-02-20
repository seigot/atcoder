N = int(input())
list = list(map(int, input().split()))

from collections import deque
q = deque()

l = []
ans = 0
 
for a in list:
    ans += 1

    if len(l) == 0:
        # 始め
        l.append([a, 1])
    elif a == l[-1][0]:
        # stackに同じ数値がある時
        l[-1][1] += 1
        if a <= l[-1][1]:
            # 数値が揃ったら破棄
            l.pop()
            ans -= a
    else:
        l.append([a, 1])

    print(ans)
