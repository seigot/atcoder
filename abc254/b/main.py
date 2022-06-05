N = int(input())
l=[[] for i in range(N)]

for i in range(N):
    length = i + 1
    for j in range(length):
        if j == 0 or j == i:
            val = 1
        else:
            val = l[i-1][j-1] + l[i-1][j]
        l[i].append(val)
#    print(*l[i])
#print(l)
for i in range(N):
     print(*l[i])
#    ll = l[i]
#    ss = str(ll[0])
#    lll = ll[1:]
#    #print(lll)
#    for j in range(len(lll)):
#        ss = ss + ' ' + str(lll[j])
#    print(ss)
