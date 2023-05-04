# 優先度付きキュー
# logNの計算量でキュー内の値を管理できる
from heapq import heappop, heappush
called = []
val = 1
heappush(called, val)
x = heappop(called)
