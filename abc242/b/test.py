import sys
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from collections import defaultdict
from bisect import bisect_right, bisect_left, insort_left, insort_right

S=input()
#s = list(set(S))
#a=S.sort()
#error(a)
s = list(set(S))
s.sort()
error(s)
ans=""
for i in s:
    #error(d[i])
    #for j in range(d[i]):
    ans = ans + i * S.count(i)

#error(ans)
print(ans)
