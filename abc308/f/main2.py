#!/usr/bin/env python3                                                                          
# 値の優先度を管理する(heap)
from heapq import heappop, heappush, heapify
a = [1,3,2,6,5]
heapify(a)
print(a)          # [1, 3, 2, 6, 5]
heappush(a, 4)    
print(a)          # [1, 3, 2, 6, 5, 4]
print(heappop(a)) # 1
print(heappop(a)) # 2
print(heappop(a)) # 3
print(heappop(a)) # 4
print(heappop(a)) # 5
print(a)          # [6]

a = [(1,9),(1,8),(1,10),(3,5),(2,5),(6,5),(5,5)]
heapify(a)
print(a)          # [(1, 8), (1, 9), (1, 10), (3, 5), (2, 5), (6, 5), (5, 5)]
heappush(a, (1,5))    
print(a)          # [(1, 5), (1, 8), (1, 10), (1, 9), (2, 5), (6, 5), (5, 5), (3, 5)]
print(heappop(a)) # (1, 5)
print(heappop(a)) # (1, 8)
print(heappop(a)) # (1, 9)
print(heappop(a)) # (1, 10)
print(heappop(a)) # (2, 5)
print(a)          # [(3, 5), (5, 5), (6, 5)]

# sort
a = [(1,9),(1,8),(1,10),(3,9),(3,8),(3,10),(2,9),(2,8),(2,10)]
print(sorted(a))                     # x満遍なくソート    [(1, 8), (1, 9), (1, 10), (2, 8), (2, 9), (2, 10), (3, 8), (3, 9), (3, 10)]
print(sorted(a, key=lambda x: x[0])) # 0番目の要素でソート [(1, 9), (1, 8), (1, 10), (2, 9), (2, 8), (2, 10), (3, 9), (3, 8), (3, 10)]
print(sorted(a, key=lambda x: x[1])) # 1番目の要素でソート [(1, 8), (3, 8), (2, 8), (1, 9), (3, 9), (2, 9), (1, 10), (3, 10), (2, 10)]

