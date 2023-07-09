l = list(map(int,input().split()))
N = l[0]
evaluation_list = l[1:]
val_max = -float("inf")
index = 0
for ii in range(N):
    val = evaluation_list[ii]
    if val > val_max:
        val_max = val
        index = ii
print(index+1)
