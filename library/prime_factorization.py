def prime_factorization(n):
    """
    task:prime factorization
    return:prime
    type:list
    """
    l=[]
    for i in range(2,int(n**0.5)+1): # 割り算のTryは2から、平方根以下まで
        while True:
            if n%i == 0:
                l.append(i) # 余り0なら素因数分解リストにappendする
                n = n//i # nの更新
            else:
                break

    if n > int(n**0.5): # nが　int(n**0.5) より大きなポイントでbreakしていたらそれをリストにappend 素数の時もこれ
        l.append(n)
    return l

# 素因数分解
A = prime_factorization(N)
# 素数をlist形式で出力 ex. [2, 2, 2, 3, 4]
print(A)
