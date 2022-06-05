N,Y=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B

for ii in range(N+1):
    for jj in range(N+1-ii):
            kk = N-ii-jj
            val = 10000*ii + 5000*jj + 1000*kk
            if val == Y:
                print(ii, jj, kk)
                exit()
print("-1 -1 -1")