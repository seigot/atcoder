N = int(input())
A = list(map(int, input().split()))
S = input()

import math
import sys
import os
from inspect import currentframe
ONLINE_JUDGE = os.environ["HOME"] == "/home/contestant"
def error(*args): # 変数の名前と値をまとめて表示
    if ONLINE_JUDGE: return
    names = {id(v): k for k, v in currentframe().f_back.f_locals.items()}
    print("[stderr]",' '.join([names.get(id(arg), '???') + ' = ' + repr(arg) for arg in args]), file=sys.stderr)

countM = [0, 0, 0]
countE = [[0] * 3 for _ in range(3)]
ans = 0

def mex(X):
    # mexを返す
    # X: 集合
    for i in range(4):
        if i not in X:
            return i
    raise Exception

for a, c in zip(A, S):
    error(a,c)
    if c == "M":
        # Mの出現個数
        countM[a] += 1
    elif c == "E":
        # Eの出現個数
        # countE[Mの値][Eの値]
        for v1 in range(3):
            countE[v1][a] += countM[v1]
    elif c == "X":
        # Xの出現個数
        # Xが出現したら
        for v1 in range(3):
            for v2 in range(3):
                ans += mex(set([v1, v2, a])) * countE[v1][v2]
print(ans)

