N,A,B=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B

l = [0]
for ii in range(1, N+1):

    s = str(ii)
    #VVVV = (ii%10000)//1000
    #VVV = (ii%1000)//100
    #VV = (ii%100)//10
    #V = ii%10

    #print(VVVV, VVV, VV, V)

    #val = VVVV + VVV + VV + V
    
    val = 0
    for jj in range(len(s)):
        val += int(s[jj])
    if val >= A and val <= B:
        l.append(ii)

print(sum(l))
