# https://atcoder.jp/contests/abc269/submissions/34946172
def main():
    n = int(input())
    left = 1
    right = n

    # 二分探索
    while right > left:
        mid = left + (right - left) // 2
        print("?", left, mid, 1, n)
        t = int(input())
        if t == -1:
            return
        if t < mid - left + 1:
            right = mid
        else:
#            left = mid
            left = mid + 1
    x = right

    # 二分探索
    left = 1
    right = n
    while right > left:
        mid = left + (right - left) // 2
        print("?", 1, n, left, mid)
        t = int(input())
        if t == -1:
            return
        if t < mid - left + 1:
            right = mid
        else:
#            left = mid
            left = mid + 1
    y = right
    print("!", x, y)


if __name__ == '__main__':
    main()
