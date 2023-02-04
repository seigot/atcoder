k = int(input())

# 素因数分解
# 素因数 p と 指数 e の組を格納
def fact(n):
  l = []
  tmp = n
  # sqrt(N)より大きい素因数は高々1つしか出ないので探索範囲を限定する
  for i in range(2,int(pow(n,0.5))+1):
    if tmp % i == 0:
      cnt = 0
      while tmp % i == 0:
        cnt += 1
        tmp //= i
      l.append([i,cnt])
  if tmp != 1:
    l.append([tmp,1])
  return l

pl = fact(k)
#print(pl)
ans = 0
# 分解した素因数が含まれる最大のN!を素因数ごとに求める
for pn,t in pl:
    rem=0
    # x ～ num*x の範囲に Nx は存在する
    for jj in range(pn,pn**t+1,pn):
        tn=jj
        # 何回pnで割れるか
        while tn%pn==0:
            tn//=pn
            rem += 1
        if rem < t:
            continue
        break

    ans=max(jj,ans)

print(ans)