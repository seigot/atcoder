N=int(input())
A=[-1]+list(map(int, input().split()))

# 累積和(逆から)
accumA = [0]*(N+2)
for ii in range(N,0,-1):
    accumA[ii] = A[ii] + accumA[ii+1]

sum1 = 0
sum2 = 0
sum3 = 0

for ii in range(1,N+1):
    #sum1
    if ii >= 2:
        sum1 += (A[ii]**2)*(ii-1)
    #sum2
    if ii <= N-1:
        sum2 += A[ii] * accumA[ii+1]
    #sum3
    if ii <= N-1:
        sum3 += (N-ii)*(A[ii]**2)

print(sum1+(-2)*sum2+sum3)
