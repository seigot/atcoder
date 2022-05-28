n,k = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
a.append(0)

ans = 0
i = 0
while True:

     # diffを求める
     diff = a[i]-a[i+1]
     # kからdiffを引いた際にまだKは残っているかどうか
     # i分引く
     k -= (i+1)*diff
     if k <= 0:
          # 残っていなければ終了処理
          k += (i+1) * diff  # 元に戻す
          tmp = k // (i+1)   # 縦の幅
          tmp2 = k % (i+1)   # 余りの幅
          # 答えを加算する
          # 平均値((a[i]+a[i+1]+1)//2) * 差分(i+1) * (i+1)
          ans += tmp * (a[i]+a[i]-tmp+1) * (i+1) //2
          ans += tmp2 * (a[i]-tmp)
          break

     # 答えを加算する
     # 平均値((a[i]+a[i+1]+1)//2) * 差分(i+1) * (i+1)
     ans += diff * (a[i]+a[i+1]+1) * (i+1) // 2
     # 次に進む
     i += 1
     if i == n:
         break

print(ans)

