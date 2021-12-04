N, D = map(int, input().split())
list = [list(map(int, input().split())) for l in range(N)]

#print(N,D,list)

list = sorted(list, reverse=False, key=lambda x: x[1])
#print(list)

ans=0
destory_col=-1
for i in range(0,N):
    target = list[i][0] # 左端に注目
    #print(target)
    if destory_col < target: # 左端が、壊した列に含まれるか
        ans += 1
        destory_col = list[i][1]+D-1 # 右側から壊す

print(ans)
