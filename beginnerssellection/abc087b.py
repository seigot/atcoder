A = int(input()) # 500
B = int(input()) # 100
C = int(input()) # 50
X = int(input())

cnt = 0

# 全探索
for aa in range(A+1):
    for bb in range(B+1):
        for cc in range(C+1):
            val = 500*aa + 100*bb + 50*cc
            if val == X:
                cnt += 1
print(cnt)