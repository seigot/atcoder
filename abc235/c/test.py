#!/bin/python

import sys
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)

N, Q = map(int, input().split())
l = list(map(int, input().split()))

from collections import defaultdict
d = defaultdict(list)

for i in range(len(l)) :
    d[l[i]].append(i)
error(d)

ans=[]
for i in range(Q):
    a, b = map(int, input().split())
    error(a, b)

    idx = d.get(int(a))
    try:
        val = idx[b-1]
        ans.append(val+1)
    except:
        ans.append(-1)

#error(l)
#error(a, b)
error(ans)
for i in range(len(ans)):
    print(ans[i])
