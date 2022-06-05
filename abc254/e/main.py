N, M = map(int, input().split()) 
edges = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split()) 
    # indexを合わす
    #a -= 1
    #b -= 1
    # 辺の情報を格納
    edges[a].append(b)
    edges[b].append(a)
Q = int(input())
#xk = [[] for i in range(Q)]
ans = [0] * Q
#print(edges)
#print(ans)

for i in range(Q):
    x, k = map(int, input().split()) 
    if k == 0:
        ans[i] = x
    if k == 1:
        sum = 0
        for j in range(len(edges[x])):
            sum += edges[x][j]
        ans[i] = sum + x
    if k == 2:
        s = set()
        # 0
        s.add(x)
        # 1
        for j in range(len(edges[x])):
            s.add(edges[x][j])
            jj = edges[x][j]
            # 2
            for kk in range(len(edges[jj])):
                s.add(edges[jj][kk])
        sum = 0
        while s:
            sum += s.pop()
        ans[i] = sum
    if k == 3:
        s = set()
        # 0
        s.add(x)
        # 1
        for j in range(len(edges[x])):
            s.add(edges[x][j])
            jj = edges[x][j]
            # 2
            for kk in range(len(edges[jj])):
                s.add(edges[jj][kk])
                ll = edges[jj][kk]
                for mm in range(len(edges[ll])):
                    s.add(edges[ll][mm])
        sum = 0
        #print(s)
        while s:
            sum += s.pop()
        ans[i] = sum

for i in range(len(ans)):
    print(ans[i])
#    xk[i].append(x)
#    xk[i].append(k)

# 今回は、次数は3
# グラフ理論における次数（じすう、英: degree, valency）は、グラフの頂点に接合する辺の数を意味
# https://ja.wikipedia.org/wiki/%E6%AC%A1%E6%95%B0_(%E3%82%B0%E3%83%A9%E3%83%95%E7%90%86%E8%AB%96)
# print(edges)