from decimal import Decimal,getcontext
getcontext().prec = 50

N = int(input())
l = [list(map(Decimal, input().split())) for l in range(N)]

pro = []
for i in range(N):
    pro.append([i+1,l[i][0]/sum(l[i])])

pro = dict(sorted(pro, key=lambda x:x[1], reverse=True))
list = []
for key, val in pro.items():
    list.append(key)
print(*list)
