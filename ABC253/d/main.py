import sys
sys.setrecursionlimit(4100000)
import math
import itertools
import collections
from heapq import heapify, heappop, heappush
from bisect import bisect, bisect_left, bisect_right
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N,A,B=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
error(N,A,B)

# 最小公倍数
def lcm(a,b):
    x = (a*b)//(math.gcd(a,b))
    return x

all_ = N*(N+1)//2

#等差数列を考えた時のN以下の最大値
end_a = N - N%A
end_b = N - N%B
end_lcm = N - N%lcm(A,B) # 最小公倍数

#print(all_)
#等差数列の和の公式使う
#a,bの公倍数部分は重複して減算してるため補填
all_ -= (A + end_a)*(end_a//A)//2
all_ -= (B + end_b)*(end_b//B)//2
all_ += (lcm(A,B) + end_lcm)*(end_lcm//lcm(A,B))//2

print(all_)