def sieve(L,R):
    if L<2: L=2
    flag=[0]*(R+1)
    for i in range(2, min(R+1,int(R**.5)+5)):
        if flag[i]:continue
        for j in range(i**2,R+1, i):
            if flag[j]:continue
            if j % i == 0: flag[j] = 1
    # return [i for i in range(L,R+1) if flag[i] == 0], flag #flagを返した方が便利な場合
    return [i for i in range(L,R+1) if flag[i] == 0]
  
N = int(input())
P = sieve(2,3*(10**5))
M = len(P)
ans = 0
for i in range(M-2):
  if P[i]**5 > N:
    break
  for j in range(i+1,M-1):
    if P[i]**2 * P[j]**3 > N:
      break
    for k in range(j+1,M):
      if P[i]**2 * P[j] * P[k] ** 2 <= N:
        ans += 1
      else:
        break
        
print(ans)