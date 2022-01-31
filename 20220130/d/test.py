from collections import deque

L = deque()
R = deque()
M = deque()

N = int(input())
S = input()

for i in range(len(S)):
    if S[i]=='L':
        R.appendleft(i)
    else:
        L.append(i)

M.append(N)
print(*(L + M + R))
