from functools import cmp_to_key

def cmp(a, b):  # a = [x_a, y_a], b = [x_b / y_b]
    # 比較対象の分数 a と b が等しければ 0 を返す
    if a[0] * b[1] == b[0] * a[1]:
        return 0
    # a, bという順で並んでほしい条件のときは-1を返し、それ以外では1を返す
    return -1 if a[0] * b[1] < b[0] * a[1] else 1

l = [[5, 7, 0], [3, 8, 2], [3, 8, 1], [1, 2, 3]]  # リストの各要素は [分子, 分母] とする
#l = sorted(l, key=lambda x:(x[1]))
l = sorted(l, key=cmp_to_key(cmp))
print(l)


A = [1,2,3]
S = "abc"
for a, c in zip(A, S):
    print(a,c)
    # 1 a
    # 2 b
    # 3 c

for ii, a in enumerate(A):
    print(ii,a)
    # 0 1
    # 1 2
    # 2 3

for ii, s in enumerate(S):
    print(ii,s)
    # 0 a
    # 1 b
    # 2 c

from itertools import accumulate
A = [0, 1,2,3]
print(list(accumulate(A))) # [0, 1, 3, 6]

