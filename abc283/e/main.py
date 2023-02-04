# https://atcoder.jp/contests/abc283/submissions/37712832
H,W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# dp[i][j][k] i行目まで決めたときの1つ前の状態がj, i行目の状態kであるときに全て繋がっている場合に操作する最小回数
# 0: そのまま
# 1: 反転
dp = [[[float('inf')] * 2 for _ in range(2)] for _ in range(H)]
dp[0][0][0] = 0 # 何も裏返さない
dp[0][0][1] = 1 # i-2個目を裏返す

# 対象行に着目した際に全てのブロックが繋がっているかどうかを返す関数
# 全て繋がっている場合はTrue、繋がっていないものが１つでもある場合はFalse
def Ok(A):
    check_flg = [0] * W
    # 各列に着目
    for j in range(W):
        a = A[1][j]
        # 上下左右
        for x, y in [[0, j], [2, j], [1, j-1], [1, j+1]]:
            if y < 0 or y > W-1:
                # 範囲外の場合は無視
                continue
            if a == A[x][y]:
                # 繋がっている場合は個数をカウント
                check_flg[j] = 1
    # 全て繋がっている場合はTrue、繋がっていないものが１つでもある場合はFalse
    return sum(check_flg) == W
    
# 全ての行に着目する(1~H-1)
for i in range(1, H):
    for j in range(2):         # i-2行目の状態(0:そのまま,1:反転) 
        for k in range(2):     # i-1行目の状態(0:そのまま,1:反転) 
            for l in range(2): # i行目の状態(0:そのまま,1:反転) 
                # x: 該当行からみて高さ方向に-2行目 
                # y: 該当行からみて高さ方向に-1行目
                # z: 該当行
                if i == 1:
                    x = [-1] * W
                else:
                    x = A[i-2]
                    if j == 1:
                        # i-2行目を反転
                        x = [1-xx for xx in A[i-2]]
                y = A[i-1] 
                z = A[i] 

                if k == 1:
                    # i-1行目を反転
                    y = [1-yy for yy in A[i-1]]
                if l == 1:
                    # i行目を反転
                    z = [1-zz for zz in A[i]]

                if i != H-1:
                    # 最後の行ではない場合
                    if Ok([x, y, z]) == True:
                        #全て繋がっている場合はDPを更新する
                        #1つ前の全て繋がっている場合の最小回数に以下の値を加算する
                        # l:現在の行を反転していたら1加算する
                        #(基本的に繋がってる状況をキープしていくので値は更新されてゆく、はず)
                        dp[i][k][l] = min(dp[i][k][l], dp[i-1][j][k]+l)
                else:
                    # 最後の行の場合
                    if Ok([x, y, z]) == True and Ok([y, z, [-1] * W]) == True:
                        #全て繋がっている場合はDPを更新する
                        #（かつ最後の行だけは、最後の行に着目した場合に繋がっている場合）
                        dp[i][k][l] = min(dp[i][k][l], dp[i-1][j][k]+l)
# 回答を得る
ans = float('inf')
for j in range(2):
    for k in range(2):
        ans = min(ans, dp[H-1][j][k])

print(-1 if ans == float('inf') else ans)