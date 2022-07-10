import math

# n までの素数テーブルを用意するclass(素数であればTrue)                                                                                                                                           
class PrimeClass:
    def __init__(self, n):
        self.max_n = n
        self.prime=[True]*(n+1)
        self.prime[0]=False
        self.prime[1]=False
        rangeMax = int(math.sqrt(n))
        for p in range(rangeMax):
            if self.prime[p] == True:
                for i in range(p*p, n+1, p):
                    self.prime[i]=False

    def isPrime(self, val):
        if val > self.max_n:
            print("value must be less than {}".format(self.max_n))
            return None
        if val > len(self.prime):
            return None
        return self.prime[val]

Prime = PrimeClass(200)
print(Prime.isPrime(10))
print(Prime.isPrime(20))
print(Prime.isPrime(23))
print(Prime.isPrime(201))
