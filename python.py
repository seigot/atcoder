#!/bin/python

import sys
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)

# input
A, B = map(int, input().split())                        # A, B
l = list(map(int, input().split()))                     # a1, a2, a3... an
l = [list(map(int, input().split())) for l in range(N)] # [[a1, b1], [a2, b2],... [aN, bN]]




# output
# error(ans)
# for i in range(len(ans)):
#     error(ans)
