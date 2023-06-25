class FenwickTree:
    # フェニック木
    # 部分和の計算と要素の更新の両方を効率的に行える木構造である
    def __init__(self, n, init_data=0): 
        # 初期化
        # n : 要素数
        # init_data : 初期値
        self.size = n
        self.tree = [0] * (n + 1)
        if init_data != 0:
            for i in range(1, n + 1):
                self.add(i, init_data)

    def sum(self, i):
        # i番目までの和を求める
        ret = 0
        i += 1
        while i > 0:
            ret += self.tree[i]
            i -= i & -i
        return ret

    def add(self, i, x):
        # i番目までの要素にxを足す
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def get(self, i):
        # i番目の要素を返す
        return self.sum(i) - self.sum(i - 1)

    def lower_bound(self, w):
        # wの境界を知る
        if w <= 0:
            return 0
        x = 0
        r = 1
        while r < self.size:
            r = r << 1
        length = r
        while length > 0:
            if length + x < self.size and self.tree[x + length] < w:
                w -= self.tree[x + length]
                x += length
            length = length >> 1
        return x

    def show(self):
        # print
        ret = []
        for i in range(self.size):
            ret.append(self.get(i))
        print(*ret)


N, M = map(int, input().split())
ft = FenwickTree(N)
ft.add(i, 1)              # 要素iに1加算
ft.sum(N - 1) - ft.sum(h) # h+1 ~ N-1までの部分和を計算