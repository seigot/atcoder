# https://atcoder.jp/contests/abc340/submissions/50158923

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
        n = len(init_val)
        self.segf = segf
        self.e = e(segf)
        self.seg_len = 1 << n.bit_length()
        self.seg = [self.e] * (self.seg_len<<1)
        for i in range(n):
            self.seg[i + self.seg_len] = init_val[i]

    def point_add(self, pos, x):
        pos += self.seg_len
        self.seg[pos] += x
        while True:
            pos >>= 1
            if not pos:
                break
            self.seg[pos] = self.segf(
                self.seg[pos << 1],  self.seg[pos << 1 | 1])

    def point_update(self, pos, x):
        pos += self.seg_len
        self.seg[pos] = x
        while True:
            pos >>= 1
            if not pos:
                break
            self.seg[pos] = self.segf(
                self.seg[pos << 1],  self.seg[pos << 1 | 1])

    def get_range(self, l, r):
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
    

    # max_rightをもとめるための条件式
    def j(self, now, i, t):
        return self.segf(now, self.seg[i]) >= t
    
    # 区間内で条件を満たせない場合-1を返す
    # そうでない場合[ql,ans)が条件を満たすような最右のansを返す
    def max_right(self,ql,qr,t):
        l = ql + self.seg_len
        r = qr + self.seg_len
        if not self.j(self.e, l, t): return -1
        left = []
        right = []
        while l < r:
            if l & 1:left.append(l); l += 1
            if r & 1:r -= 1; right.append(r)
            l >>= 1; r >>= 1
        ord = left + right[::-1]
        now = self.e
        pos = -1
        for i in ord:
            if self.j(now, i, t):
                now = self.segf(now, self.seg[i])
            else:
                pos = i
                break
        if pos == -1:return qr
        while True:
            if pos >= self.seg_len:break
            pos <<= 1
            if self.j(now, pos, t):
                now = self.segf(now, self.seg[pos])
                pos += 1
        return pos - self.seg_len
    
    # 区間内で条件を満たせない場合-1を返す
    # そうでない場合(ans,qr)が条件を満たすような最左のansを返す
    def min_left(self,ql,qr,t):
        l = ql + self.seg_len
        r = qr + self.seg_len
        if not self.j(self.e, r-1, t): return -1
        left = []
        right = []
        while l < r:
            if l & 1:left.append(l); l += 1
            if r & 1:r -= 1; right.append(r)
            l >>= 1; r >>= 1
        ord = left + right[::-1]
        now = self.e
        pos = -1
        for i in ord[::-1]:
            if self.j(now, i, t):
                now = self.segf(now, self.seg[i])
            else:
                pos = i
                break
        if pos == -1:return ql-1
        while True:
            if pos >= self.seg_len:break
            pos = (pos<<1) + 1
            if self.j(now, pos, t):
                now = self.segf(now, self.seg[pos])
                pos -= 1
        return pos - self.seg_len

    # ------ dual -------
    def range_add(self, l, r, x):
        l += self.seg_len
        r += self.seg_len
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
        pos += self.seg_len
        res = self.seg[pos]
        while True:
            pos >>= 1
            if not pos:
                break
            res = self.segf(res, self.seg[pos])
        return res

# 引数1:区間の更新、値の取得を行う(add)
st = SegTree(add, A)

#ball = st.get_point(v)     # 値を取得する時は st.get_point(index)    #(get_range()ではない)
#st.range_add(0, N+1, loop) # 値を加算する時は、st.range_add(l,r,val) #(point_update()ではない)
