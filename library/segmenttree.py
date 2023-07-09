# https://qiita.com/takayg1/items/c811bd07c21923d7ec69
# 区間の最小値、最大値を求めたい、区間の和を求めたいなど、の際に使用する、logNで計算できる

# -----
def add(x, y):
    return x + y

def e(a):
    if a == min:
        return 10**18
    if a == max:
        return -10**18
    if a == add:
        return 0

class SegTree:
    def __init__(self, segf, init_val):
        # 初期化
        # 引数1:区間の最小/最大の値を返す(min/max)
        # 引数2:区間の配列初期値（ex.最小にする場合は[10**18]*n）
        n = len(init_val)
        self.segf = segf
        self.e = e(segf)
        self.seg_len = 1 << n.bit_length()
        self.seg = [self.e] * 2*self.seg_len

        for i in range(n):
            self.seg[i + self.seg_len] = init_val[i]
        for i in range(self.seg_len)[::-1]:
            self.seg[i] = segf(self.seg[i << 1], self.seg[i << 1 | 1])

    def point_add(self, pos, x):
        # 位置posの値を更新する(x加算する)
        pos += self.seg_len
        self.seg[pos] += x
        while True:
            pos >>= 1
            if not pos:
                break
            self.seg[pos] = self.segf(
                self.seg[pos << 1],  self.seg[pos << 1 | 1])

    def point_update(self, pos, x):
        # 位置posの値を更新する(xにする)
        pos += self.seg_len
        self.seg[pos] = self.segf(self.seg[pos],x)
        while True:
            pos >>= 1
            if not pos:
                break
            self.seg[pos] = self.segf(
                self.seg[pos << 1],  self.seg[pos << 1 | 1])

    def get_range(self, l, r):
        # 区間（l,r）のmin/max/sumなどの値を取得する(segfに依存する)
        l += self.seg_len
        r += self.seg_len
        res = self.e
        while l < r:
            if l & 1:
                res = self.segf(res, self.seg[l])
                l += 1
            if r & 1:
                r -= 1
                res = self.segf(res, self.seg[r])
            l >>= 1
            r >>= 1
        return res

    # ------ range_add & get_point -------
    def range_add(self, l, r, x):
        # 区間(l,r)の値を更新する(x加算する)、と思う
        l += self.seg_len
        r += self.seg_len
        self.seg[l] += x
        self.seg[r] += x
        while l < r:
            if l & 1:
                self.seg[l] = self.segf(x, self.seg[l])
                l += 1
            if r & 1:
                r -= 1
                self.seg[r] = self.segf(x, self.seg[r])
            l >>= 1
            r >>= 1

    def get_point(self, pos):
        # posの値を返す
        pos += self.seg_len
        res = self.seg[pos]
        while True:
            pos >>= 1
            if not pos:
                break
            res = self.segf(res, self.seg[pos])
        return res

# 引数1:区間の最小/最大の値を返す(min/max)
# 引数2:区間の配列初期値（ex.最小にする場合は[10**18]*n）
st = SegTree(min, [10**18]*n)
#mini = st.get_range(0,compy[y])
#st.point_update(compy[y], z)