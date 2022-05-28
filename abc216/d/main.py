from collections import defaultdict, deque
from typing import DefaultDict, Deque, List

# https://atcoder.jp/contests/abc216/submissions/30993543

N, M = map(int, input().split())

cyls: List[Deque[int]] = []
colorIdx: DefaultDict[int, List[int]] = defaultdict(list)
either = set()
both = set()

for idx in range(M):
    K = int(input())
    A = deque(map(int, input().split()))

    head = A.popleft()
    cyls.append(A)
    colorIdx[head].append(idx)
    if len(colorIdx[head]) == 2:#head in either:
        either.remove(head)
        both.add(head)
    else:
        either.add(head)

action = 0
while both:
    a, b = colorIdx[both.pop()]
    for idx in [a, b]:
        if not cyls[idx]:
            continue
        head = cyls[idx].popleft()
        colorIdx[head].append(idx)
        if len(colorIdx[head]) == 2:#head in either: head in either:
            either.remove(head)
            both.add(head)
        else:
            either.add(head)
    action += 1

if action == N:
    res = 'Yes'
else:
    res = 'No'
    #res = 'Yes' if all(not cyl for cyl in cyls) else 'No'
print(res)
