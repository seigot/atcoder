# 距離の 2 乗を計算する関数
def dist_sq(a, b, c, d):
  return (a - c) ** 2 + (b - d) ** 2
# 答えを求める関数
def solve(x1, y1, x2, y2):
  for x in range(x1 - 2, x1 + 3):
    for y in range(y1 - 2, y1 + 3):
      if dist_sq(x, y, x1, y1) == dist_sq(x, y, x2, y2) == 5:
        return "Yes"
  return "No"
x1, y1, x2, y2 = map(int, input().split())
print(solve(x1, y1, x2, y2))


