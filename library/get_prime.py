def prime(N):
    # https://gembanoqcqa.com/python-primes/
    primes = []
    for i in range(2, N + 1):
        primes.append(i)
        for p in range(2, i):
            if i % p == 0:
                primes.remove(i)
                break
    return primes
# Nまでの素数リストを取得
l = prime(N)
