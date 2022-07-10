import math

# n までの素数テーブルを用意するclass(素数であればTrue)
# n-1までの整数が素数かどうかを判定する
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
        if val >= len(self.prime)-1:
            return None
        return self.prime[val]

Prime = PrimeClass(200)
print(Prime.isPrime(197))
print(Prime.isPrime(198))
print(Prime.isPrime(199))
print(Prime.isPrime(200))
print(Prime.isPrime(202))
print(Prime.isPrime(201))

print("---")
Prime2 = PrimeClass(4)
print(Prime2.isPrime(2))
print(Prime2.isPrime(3))
print(Prime2.isPrime(4))

print("---")
Prime2 = PrimeClass(5)
print(Prime2.isPrime(2))
print(Prime2.isPrime(3))
print(Prime2.isPrime(4))
