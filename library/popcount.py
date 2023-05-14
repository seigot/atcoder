def popcnt(n):
    # popcount
    # 2進数の数のうち、"1"の数を高速に数える
    # https://zenn.dev/kiwamachan/articles/ad17cc11f4ad55
    c = (n & 0x5555555555555555) + ((n >> 1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
    c = (c & 0x0f0f0f0f0f0f0f0f) + ((c >> 4) & 0x0f0f0f0f0f0f0f0f)
    c = (c & 0x00ff00ff00ff00ff) + ((c >> 8) & 0x00ff00ff00ff00ff)
    c = (c & 0x0000ffff0000ffff) + ((c >> 16) & 0x0000ffff0000ffff)
    c = (c & 0x00000000ffffffff) + ((c >> 32) & 0x00000000ffffffff)
    return c

a = 255
v = popcnt(a)
print(v) # 8

a = 1
v = popcnt(a)
print(v) # 1

a = 3
v = popcnt(a)
print(v) # 2

a = 4
v = popcnt(a)
print(v) # 1
