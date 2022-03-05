import sys
input = lambda: sys.stdin.readline().rstrip()
 
P = 998244353
 
def calc(A):
    ret = 0
    for a in A:
        ret = (ret * 26 + a) % P
    return ret

T = int(input())
for _ in range(T):
    N = int(input())
    S = [ord(a) - 65 for a in input()]
    L = S[:N//2]
    R = S[-(N//2):]
    adj = 1
    if L[::-1] > R:
        adj = 0
    if N % 2 == 0:
        print((calc(L) + adj) % P)
    else:
        m = S[N//2]
        print((calc(L) * 26 + m + adj) % P)
