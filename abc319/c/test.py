
from collections import defaultdict, deque, Counter

d = defaultdict(int)
d[-1] += 1
d[3] += 1
d[5] += 1
d[5] -= 1
for ii in d.keys():
    if d[5] >= 2 and d[3] == 3 and d[ii] >= 1 and d[100] >= 1 and d[101] == 1:
        print("hoge")
    print(ii)
print(d)
print(sum(d.values()))


print("---")
x = 0
y = 3
z = 6
print(x^y^z)
print(x^y)
print(y^z)
print(z^z)
x = 0
y = 3
z = 3
print(x^y^z)
x = 3
y = 3
z = 0
print(x^y^z)
print(x^y)
print(y^z)
print(z^z)
