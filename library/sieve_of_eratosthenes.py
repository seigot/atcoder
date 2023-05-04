def primes(x):
    # 0以上整数x「未満」の素数をリストに格納して返す
    # https://nekotheshadow.github.io/qiita-backup/blog/4ebad619564a48f5a97f/
    if x < 2: return []

    primes = [i for i in range(x)]
    primes[1] = 0 # 1は素数ではない

    # エラトステネスのふるい
    for prime in primes:
        if prime > math.sqrt(x): break
        if prime == 0: continue
        for non_prime in range(2 * prime, x, prime): primes[non_prime] = 0
    return [prime for prime in primes if prime != 0]

# 0以上整数N「未満」の素数をリストに格納して返す
l = primes(N)
