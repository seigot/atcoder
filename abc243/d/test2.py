N, X = map(int, input().split())
S = input()
L = []
for s in S:
    if len(L) == 0:
        L.append(s)
    elif L[-1] == "U":
        L.append(s)
    elif s == "U":
        L.pop(-1) 
    else:
        L.append(s)
for l in L:
    if l == "U":
        if X != 1:
            X //= 2
    elif l == "L":
        X *= 2
    else:
        X += X+1
print(X)
