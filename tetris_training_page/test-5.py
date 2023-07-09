S = int(input())

from collections import defaultdict
# rotate
rotate_maxd = defaultdict(int)
rotate_maxd[1] = 2
rotate_maxd[2] = 4
rotate_maxd[3] = 4
rotate_maxd[4] = 4
rotate_maxd[5] = 1
rotate_maxd[6] = 2
rotate_maxd[7] = 2

N = rotate_maxd[S]
st = ""
for ii in range(N):
    st += str(ii)
print(st)
