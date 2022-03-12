import sys
N=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)

error(N,A,B) 

ans1=0
for i in range(N):
    if A[i] == B[i]:
        ans1 += 1

A_set = set(A)
B_set = set(B)
AB = A_set & B_set
ans2 = len(AB) - ans1

print(ans1)
print(ans2)
