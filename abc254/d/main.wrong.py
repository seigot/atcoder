N = int(input())

l_sqrt = []
for i in range(2*10**5):
    val = i*i
    if val < N:
        l_sqrt.append(val)
    else:
        break

def prime(a):#aが素数であるかどうかを判定する関数
    for i in range(2,a):
        if a % i == 0: #割り切れれば、0を返す
            return 0
    return 1 #素数の場合は、1を返す

def prime_factorization(a):#aを素因数分解する関数
    list_prime = [] #素因数を格納するリストを用意する
    for i in range(2,a):
        if prime(i):
            while True:
                if a % i == 0: #素数で割り切れるかどうかを調べる
                    list_prime.append(i) #割り切れる場合は、リストにその素数を追加する
                    a /= i
                else:
                    break
    if(len(list_prime) == 0): #a自体が素数の場合は、その数をそのまま返す
        return a
    return list_prime #リストを返す

for i in range(len(l_sqrt)):
    ll = prime_factorization(l_sqrt[i])
    print(ll)