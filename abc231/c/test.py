from bisect import bisect_left,bisect_right

A = [10,20,30,40,50]
A.sort()

idx_l = bisect_left(A, 20)
idx_r = bisect_right(A, 20)
print(idx_l, idx_r)
idx_l = bisect_left(A, 15)
idx_r = bisect_right(A, 15)
print(idx_l, idx_r)

x1 = (-7)//3
x2 = (-7)%3
x3 = ((-3)-(2))%3
print(x1, x2, x3)
