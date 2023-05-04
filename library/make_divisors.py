def make_divisors(n):
    # 約数列挙
    # https://qiita.com/LorseKudos/items/9eb560494862c8b4eb56
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
# 入力値=Nの約数を返す
# 8 => [2,2,2]
make_divisors(N)

