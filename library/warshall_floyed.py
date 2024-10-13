#ワーシャルフロイド法:c[i][j]:iからjまでの最小距離を二次元配列で返す
# cc[ii][jj]: iiからjjまでの距離
def Warshall_Floyd(n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                c[i][j] = min(c[i][j],c[i][k]+c[k][j])
Warshall_Floyd(n)
