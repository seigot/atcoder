def primesLR(L,R):
    if L<2: L=2
    flag=[0]*(R+1)
    for i in range(2, min(R+1,int(R**.5)+5)):
        if flag[i]:continue
        for j in range(i**2,R+1, i):
            if flag[j]:continue
            if j % i == 0: flag[j] = 1
    # return [i for i in range(L,R+1) if flag[i] == 0], flag #flagをèしたæがäåなåå
    return [i for i in range(L,R+1) if flag[i] == 0]
  
# L~Rまでの素数を列挙する(ex.2~3*(10**5))
# 場合の数を求める時は大きな数を早々に探索打ち切ると高速である場合が多い
P = primesLR(0,3*(10**5)) 

