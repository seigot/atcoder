n = int(input())
l = 1
r = n
while r - l > 1:
    m = (r+l)//2
    print("?", m)
    tmp = int(input())
    if tmp == 0:
        l = m
    else:
        r = m
print("!",l)
