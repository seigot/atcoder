N, X = map(int, input().split())
S = input()
L = []

print(S)
print(S[::])
print(S[::-1])
print(*S[::])
print(*S[::-1])
for i in range(len(S)):
    s = S[i]
    if len(L) == 0: # 空の時はそのままappend
        L.append(s)
    elif s == "U" and L[-1] != "U": # 終端が"L"or"R"の時はそのままappend
        L.pop(-1) 
    else:
        L.append(s)

print(L)
print(L[::])
print(L[::-1])
print(*L[::])
print(*L[::-1])
for l in L:
    if l == "U":
        if X != 1:
            X //= 2
    elif l == "L":
        X *= 2
    else:
        X += X+1
print(X)
