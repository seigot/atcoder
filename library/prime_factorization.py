# https://atcoder.jp/contests/abc342/submissions/50619066
# https://atcoder.jp/contests/abc342/submissions/50584195
class Era:
    def __init__(self, n):
        self.N = n
        self.l = [i for i in range(n+1)]
        for i in range(2,min(n,n//2+10)):
            if self.l[i] == i:
                for p in range(i+i,n+1,i):
                    if self.l[p] == p:
                        self.l[p] = i
    # 素数判定
    def isprime(self,n):
        return self.l[n] == n

    # 素因数分解
    def primes(self,n):
        ans = []
        now = n
        while now != 1:
            if not ans:
                ans.append([self.l[now], 1])
            else:
                if ans[-1][0] == self.l[now]:
                    ans[-1][1] += 1
                else:
                    ans.append([self.l[now], 1])
            now //= self.l[now]
        return ans
    
    # 約数列挙
    def facts(self,n):
        pf = self.primes(n)
        ans = [1]
        for pn, cnt in pf:
            tmp = [pow(pn, i) for i in range(1, cnt+1)]
            m = len(ans)
            for num in tmp:
                for i in range(m):
                    ans.append(ans[i]*num)
        return ans

# class定義
era = Era(2*10**5+10)
# 素因数分解
# 2の3乗の場合=[2,3]と表現できる
f = era.primes(8)  # [2,3]
