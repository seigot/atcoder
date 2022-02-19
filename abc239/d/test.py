# 200までの素数を事前に用意する(素数であればTrue)
prime=[True]*201
prime[0]=False
prime[1]=False
for p in range(15):
    if prime[p] == True:
        for i in range(p*p, 201, p):
            prime[i]=False

A, B, C, D=map(int,input().split())

for x in range(A, B+1):
    isAllNoPrimeNumber = True
    for y in range(C, D+1):
        # x + y の組み合わせを確認する
        # --> 素数である組み合わせが1つでもあればその数は選択不可である
        # --> 素数である組み合わせが1もなければ選択する
        if prime[x + y] == True:
            isAllNoPrimeNumber = False

    if isAllNoPrimeNumber == True:
        print("Takahashi")
        exit()
print("Aoki")

        
