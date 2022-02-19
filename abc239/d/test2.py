import math

# n までの素数テーブルを用意するclass(素数であればTrue)
class PrimeClass:
    def __init__(self, n):
        self.prime=[True]*(n+1)
        self.prime[0]=False
        self.prime[1]=False
        rangeMax = int(math.sqrt(n))
        for p in range(rangeMax):
            if self.prime[p] == True:
                for i in range(p*p, n+1, p):
                    self.prime[i]=False

    def isPrime(self, val):
        if val > len(self.prime):
            return None
        return self.prime[val]

A, B, C, D=map(int,input().split())

# 200までの素数を事前に用意する(素数であればTrue)
Prime = PrimeClass(200)

print(Prime.isPrime(10))
print(Prime.isPrime(20))
print(Prime.isPrime(23))

for x in range(A, B+1):
    isAllNoPrimeNumber = True
    for y in range(C, D+1):
        # x + y の組み合わせを確認する
        # --> 素数である組み合わせが1つでもあればその数は選択不可である
        # --> 素数である組み合わせが1もなければ選択する
        if Prime.isPrime(x + y) == True:
            isAllNoPrimeNumber = False

    if isAllNoPrimeNumber == True:
        print("Takahashi")
        exit()
print("Aoki")

        
