N = int(input())
A = []
for ii in range(N):
    A.append(int(input()))

s = set()

for ii in range(len(A)):
    s.add(A[ii])
print(len(s))