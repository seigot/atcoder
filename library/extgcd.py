def extgcd(a,b):
    # 拡張ユークリッドの互除法
    # ax+by=±gcd(a,b) となる整数の組 (x,y) を O(logmin(∣a∣,∣b∣)) で計算する
    if b == 0:
        return 1,0,a
    q,r = a//b, a%b
    x,y,d = extgcd(b,r)
    s,t = y, x-y*q
    return s,t,d

# (0,0),(A,B),(X,Y)を頂点とする三角形の面積は、|AY - BX|/2
# --> |AY - BX| == 2 となる(A,B)を見付けたい
# 拡張ユークリッドの互除法
# (X,Y) = (3,5) --> (A, B, d) = (-1, -2, 1)
a,b,d = extgcd(y, -x)
if d < 0:
    a *= -1
    b *= -1
    d *= -1
if d == 1:
    print(a*2,b*2)
elif d == 2:
    print(a,b)
else:
    print(-1)
