N = int(input())
l = [[] for _ in range(N)]

for ii in range(N):
    t,x,y=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
    l[ii].append(t)
    l[ii].append(x)
    l[ii].append(y)

current_t = 0
current_x = 0
current_y = 0
for ii in range(len(l)):

    # get next coordinate    
    t = l[ii][0]
    x = l[ii][1]
    y = l[ii][2]

    # diff
    diff_t = t - current_t
    diff_x = x - current_x
    diff_y = y - current_y

    #print(diff_t, diff_x, diff_y)
    # 距離
    dist = abs(diff_x) + abs(diff_y)
    diff = diff_t - dist
    if diff < 0:
        # 足りないケース
        print("No")
        exit()
    if diff == 0:
        pass
    if diff > 0:
        # 行きすぎて戻れないケース
        if diff%2 != 0:
            print("No")
            exit()
    # update
    current_t = t
    current_x = x
    current_y = y

print("Yes")