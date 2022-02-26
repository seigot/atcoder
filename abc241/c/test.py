N = int(input())
S=[]
for i in range(N):
    S.append(input())

ans="No"
for i in range(N): #横
    for j in range(N): #縦
        # 横に着目→
        cnt=0
        if i < N-5:
            for k in range(6):
                if S[j][i+k] == '#':
                    cnt+=1
            if cnt >= 4:
                ans="Yes"

        cnt=0
        # 縦に着目↓
        if j < N-5:
            for k in range(6):
                if S[j+k][i] == '#':
                    cnt+=1
            if cnt >= 4:
                ans="Yes"

        cnt=0
        # 斜めに着目/
        if i < N-5 and j < N-5:
            for k in range(6):
                if S[j+k][i+k] == '#':
                    cnt+=1
            if cnt >= 4:
                ans="Yes"

        # 斜めに着目/
        cnt = 0
        if i >= 5 and j < N-5:
            for k in range(6):
                if S[j+k][i-k] == '#':
                    cnt+=1
            if cnt >= 4:
                ans="Yes"

print(ans)
