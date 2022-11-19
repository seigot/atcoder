N = int(input())
A = list(map(int,input().split()))
ans = 0
mod = 998244353
for cnt in range(1,N+1):

    dp = [[[0 for jj in range(cnt)] for kk in range(cnt+1)] for ll in range(N+1)]
    # dp[j][k][l] : Aの先頭j項からk個の項を選ぶ方法であって、選んだ項の総和をiで割った余りがlとなるようなものの個数
    #               (j項目まででk個選んで総和をiで割ったあまりがl)
    dp[0][0][0] = 1

    # 先頭~jjまでみたとき
    for jj in range(N):
        # kk個取得するタイミングで
        for kk in range(cnt+1):
            # 余りがllとなるもの
            for ll in range(cnt):
                ## 先頭~(jj-1)までみたときに、kk-1個取得した状態から
                ## 現在着目しているものを加えたもの
                # 更新のために引き継ぐ
                dp[jj+1][kk][ll] += dp[jj][kk][ll]
                if kk != cnt:
                    # 通常の更新, kk==cntの場合は
#                    dp[jj+1][kk+1][(A[jj]+ll)%cnt] += dp[jj][kk][ll]
                    dp[jj+1][kk+1][ll] += dp[jj][kk][(A[jj]-ll)%cnt]

    dp[N][cnt][0] %= mod
    ans += dp[N][cnt][0]
    ans %= mod
print(ans%mod)
