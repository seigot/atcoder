n = 10
for i in range(n):
    print(i)  # 0,1,2,3...9
for i in range(n)[::-1]:
    print(i)  # 9,8,7,6...0
for i in range(n-1,-1,-1):
    print(i)  # 9,8,7,6...0

a,b,c = 1,2,3
print(a,b,c)  # 1,2,3
a,b,c = c,a,b
print(a,b,c)  # 3,1,2
