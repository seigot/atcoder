#!/usr/bin/env pypy3
from collections import Counter, deque, defaultdict
from itertools import permutations, combinations, accumulate
from functools import lru_cache
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heapify, heappush, heappop
from array import array
from decimal import Decimal
from copy import deepcopy
from string import ascii_uppercase, ascii_lowercase, ascii_letters
from math import factorial, floor, ceil
import math
import sys
sys.setrecursionlimit(1<<30)

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    N = int(readline())
    ans = ''
    while N:
        q, r = divmod(N, 2)
        if r:
            ans += 'A'
            N -= 1
        else:
            ans += 'B'
            N = q
    print(ans[::-1])

if __name__ == '__main__':
    main()
