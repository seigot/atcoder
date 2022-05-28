import sys
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from collections import defaultdict
from bisect import bisect_right, bisect_left, insort_left, insort_right
from collections import defaultdict, deque

N, M=map(int, input().split())
dqlist = []
headd = [[] for _ in range(N+1)]
headcnt = defaultdict(int)
cnt2queue = deque()
error(N, M)
for i in range(M):
    k = input()
    dq = deque(map(int, input().split()))
    dqlist.append(dq)
    idx = i
#    val = dqlist[idx].popleft()
    val = dqlist[idx][0]
    headd[val].append(idx)
    error("headd", headd)
    if len(headd[val]) == 2:
        cnt2queue.append(headd[val])

#error(headd)
#error(headcnt)
#error("dqlist", dqlist)
#error("cnt2queue", cnt2queue)

action = 0
while cnt2queue:
#    error("cnt2queue", cnt2queue)
    popval, popval2 = cnt2queue.popleft()
#    error("action", action)
#    error("popval", popval, popval2)
#    error("dqlist", dqlist)

    # pop
    idx = popval
    val = dqlist[idx-1].popleft()
    if dqlist[idx-1]:
#        error("headd", headd)
#        error("indexes", indexes)
#        error("len(indexes)", len(indexes))
        val = dqlist[idx-1][0]
        headd[val].append(idx)
        if len(headd[val]) == 2:
            cnt2queue.append(headd[val])
    idx = popval2
    val = dqlist[idx-1].popleft()
    if dqlist[idx-1]:
        val = dqlist[idx-1][0]
        headd[val].append(idx)
#        error("headd[val]", headd[val])
        if len(headd[val]) == 2:
            cnt2queue.append(headd[val])

#    error("cnt2queue", cnt2queue)
    action += 1

if action == N:
    print("Yes")
else:
    print("No")
