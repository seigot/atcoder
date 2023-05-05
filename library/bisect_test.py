#!/usr/bin/env python3                                                                          
from bisect import bisect_left, bisect_right
ll = [0,2,4,6,8]
l = 3
r = 7
left = bisect_left(ll,l)   # lが出現する1つ前のindex
right = bisect_right(ll,r) # rが出現するindex
print(left,right) # 2 4