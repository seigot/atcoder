h,w,n = map(int, input().split())
#二次元累積和
ab = [[0]*(w+1) for _ in range(h+1)] # 穴の部分
c = [[0]*(w+1) for _ in range(h+1)]  # 二次元累積和 c[jj][ii] 座標(jj,ii)までに存在する穴の数
for _ in range(n):
  a,b = map(int, input().split())
  c[a][b] = 1
  ab[a][b] = 1

# 横方向の累積和（座標(j,i)までに存在する穴の個数の累積和...のy座標方向の更新）
for i in range(h+1):
  for j in range(1,w+1):
    c[i][j] += c[i][j-1]

# 縦方向の累積和（座標(j,i)までに存在する穴の個数の累積和...のx座標方向の更新）
for j in range(w+1):
  for i in range(1,h+1):
    c[i][j] += c[i-1][j]


ans = 0
for i in range(1,h+1):
  for j in range(1,w+1):
    # 左上が(i,j) である一辺がk の穴のない正方形を作れるか?を考える
    # 左上が(i,j)==0である場合のみ探索する
    # 穴の数の累積和は単調増加なので二分探索を使う事が可能である
    if ab[i][j] == 0:
      #二分探索
      l = 0      # 辺の大きさ(min)
      r = 3010   # 辺の大きさ(max)
      while r-l>1:
        m = (r+l)//2
        if i+m <= h and j+m <= w:
          check = c[i+m][j+m] - c[i+m][j-1] - c[i-1][j+m] + c[i-1][j-1] 
          # (i+m, j+m)までの累積和 から (i,j)までの累積和を求める。（二次元で）
          if check == 0:
            l = m
          else:
            r = m
        else:
          r = m
      # 左上が(i,j)である正方形の数を足す
      ans += l+1

print(ans)