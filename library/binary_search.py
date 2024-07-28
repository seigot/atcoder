
_A = sorted(A)

def get_num(b,d):
    num = -1
    # Aに含まれる個数
    id_u = bisect_right(_A, b+d)
    id_l = bisect_left(_A, b-d)
    num = id_u - id_l

    return num


# 二分探索
# b: （最終的に出力に使いたい）基準値
# k: （最終的に出力に使いたい）基準値
def binary_search(b,k):
    lowwer = -1          # lowest
    upper = 10**18 + 10  # highest

    while upper - lowwer > 1:
        mid = (upper + lowwer)//2
        # 評価関数を用意して、基準よりも大きいか小さいかを判断する
        # 基準よりも大きい場合は、highestの方の探索範囲を小さくする
        # 基準よりも小さい場合は、lowestの方の探索範囲を大きくする
        n = get_num(b,mid) # 評価関数
        if n >= k:         # 判断基準
            upper = mid
        else:
            lowwer = mid
    return upper


for ii,bb in enumerate(B):
    bj = bb[0]
    kj = bb[1]
    d = binary_search(bj,kj)
    print(d)