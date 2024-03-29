
# https://qiita.com/nishizumi_noob/items/7a1323c45cf6ce56a368
from functools import cmp_to_key

def cmp(a, b):  # a = [x_a, y_a], b = [x_b / y_b]
    # 比較対象の分数 a と b が等しければ 0 を返す
    if a[0] * b[1] == b[0] * a[1]:
        return 0
    # a, bという順で並んでほしい条件のときは-1を返し、それ以外では1を返す
    return -1 if a[0] * b[1] < b[0] * a[1] else 1
    # 降順にしたい場合は、不等号をかえる
    #return -1 if a[0] * b[1] > b[0] * a[1] else 1

l = [[5, 7], [3, 8], [1, 2]]  # リストの各要素は [分子, 分母] とする
l = sorted(l, key=cmp_to_key(cmp))
print(l) # l = [[3, 8], [1, 2], [5, 7]]

from functools import cmp_to_key
def cmp(a, b):  # a = [x_a, y_a], b = [x_b / y_b]
    # 比較対象の分数 a と b が等しければ 0 を返す
    if a[0] * b[1] == b[0] * a[1]:
        ## [2]にidがある場合
        if len(a) == 3:
            if a[2] < b[2]:
                # 同じa,bにindexがある場合indexの小さい順に並び替える 
                return -1
        return 0
    # a, bという順で並んでほしい条件のときは-1を返し、それ以外では1を返す
    return -1 if a[0] * b[1] > b[0] * a[1] else 1
l = [[5, 7], [3, 8], [3, 8], [1, 2]]  # リストの各要素は [分子, 分母] とする
l = sorted(l, key=cmp_to_key(cmp))
print(l) # [5, 7], [1, 2], [3, 8], [3, 8]]
l = [[5, 7, 1], [3, 8, 3], [3, 8, 2], [1, 2, 4]]  # リストの各要素は [分子, 分母] とする
l = sorted(l, key=cmp_to_key(cmp))
print(l) # [[5, 7, 1], [1, 2, 4], [3, 8, 2], [3, 8, 3]]