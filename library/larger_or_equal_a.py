# aの倍数でb以上の数
def f(a, b):
    x = ((b - 1) // a + 1) * a
    return x
print(f(25,50)) # 50
