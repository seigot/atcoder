l = list(map(int,input().split()))
S = l[0]
D = l[1]

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
D %= rotate_maxd[S]

# range
ranged = defaultdict(list)
# I mino
ll = []
ll.append([0,1,2,3,4,5,6,7,8,9])
ll.append([2,3,4,5,6,7,8])
ranged[1] = ll
# L mino
ll = []
ll.append([0,1,2,3,4,5,6,7,8])
ll.append([1,2,3,4,5,6,7,8])
ll.append([1,2,3,4,5,6,7,8,9])
ll.append([1,2,3,4,5,6,7,8])
ranged[2] = ll
# J mino
ll = []
ll.append([1,2,3,4,5,6,7,8,9])
ll.append([1,2,3,4,5,6,7,8])
ll.append([0,1,2,3,4,5,6,7,8])
ll.append([1,2,3,4,5,6,7,8])
ranged[3] = ll
# T mino
ll = []
ll.append([0,1,2,3,4,5,6,7,8])
ll.append([1,2,3,4,5,6,7,8])
ll.append([1,2,3,4,5,6,7,8,9])
ll.append([1,2,3,4,5,6,7,8])
ranged[4] = ll
# O mino
ll = []
ll.append([0,1,2,3,4,5,6,7,8])
ranged[5] = ll
# S mino
ll = []
ll.append([1,2,3,4,5,6,7,8])
ll.append([0,1,2,3,4,5,6,7,8])
ranged[6] = ll
# Z mino
ll = []
ll.append([1,2,3,4,5,6,7,8])
ll.append([0,1,2,3,4,5,6,7,8])
ranged[7] = ll

ans = ranged[S][D]
st = ""
for a in ans:
    st += str(a)
print(st)

