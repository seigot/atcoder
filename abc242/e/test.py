import sys
#input = input()lambda: sys.stdin.readline().rstrip()
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)

P = 998244353

def calc(A):
    # 入力文字列Sの中央より左側をAとする。
    # 文字列Aと同じ、もしくは、それより小さい回文の数を数える。
    ret = 0
    for a in A:
        #error(a)
        a -= 1
        # AAA.. の場合は0+1通り
        # ABA.. の場合は(1+26)+1通り
        ret = (a + ret * 26) % P
    return ret

T = int(input())
for _ in range(T):
    N = int(input())
    S = [ord(a) - (ord("A") - 1) for a in input()] # 数値列に直す    
#    error(S)
    S_L = S[:N//2]    # Sの左半分を取得
    S_R = S[-(N//2):] # Sの右半分を取得
#    error(S_L)
#    error(S_R)
#    error(S_L[::-1]) # Lの反転

    # 争点?
    adj = 1
    if S_R < S_L[::-1]:
        # RがLを反転させた場合より小さい場合は、
        # 争点が条件を満たさないので1を引く。値は0になる。
        adj = 0

    if N % 2 == 0:  # 偶数の場合
        print((calc(S_L) + adj) % P)
    else:           # 奇数の場合
        m = S[N//2] # 中央の文字を取得
        m -= 1
        # 桁が一つ大きいので、
        # 直前の回文の数*26と、中央の文字、それに加えて争点が条件を満たす場合はadj加算する
        print((calc(S_L) * 26 + m + adj) % P)
