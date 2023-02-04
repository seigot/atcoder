import sys
INF = 10**9
def main():
    input = sys.stdin.readline
    H, W = map(int, input().split())
    A = [tuple(map(int, input().split())) for _ in range(H)]
    B = [[2] * (W + 2)]
    for a in A:
        B.append([2] + list(a) + [2])
    B.append([2] * (W + 2))
    dp = [[[0] * 2 for _ in range(2)] for _ in range(2)]

    for i in range(1, H + 1):
        ndp = [[[INF] * 2 for _ in range(2)] for _ in range(2)]
        for f0 in range(2):
            for f1 in range(2):
                for f2 in range(2):
                    # check
                    for j in range(1, W + 1):
                        now = 0
                        # check: 4方向に繋がりがある場合は孤立していないと判断可能
                        now += 1 if B[i][j - 1] == B[i][j] else 0
                        now += 1 if B[i][j] == B[i][j + 1] else 0
                        now += 1 if B[i - 1][j] ^ f0 == B[i][j] ^ f1 else 0
                        now += 1 if B[i][j] ^ f1 == B[i + 1][j] ^ f2 else 0
                        if now == 0: break
                    else:
                        # 孤立している場合はその最小値をカウントする
                        # 
                        for f3 in range(2):
                            ndp[f0][f1][f2] = min(ndp[f0][f1][f2],      # これまでの値
                                                  dp[f3][f0][f1] + f1)  # 今回裏返すかどうか
        dp = ndp
    ans = INF
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ans = min(ans, dp[i][j][k])
    return ans if ans < INF else -1

if __name__ == '__main__':
    print(main())
