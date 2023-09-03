Ha, Wa = map(int, input().split())
A = [list(input()) for _ in range(Ha)]
Hb, Wb = map(int, input().split())
B = [list(input()) for _ in range(Hb)]
Hx, Wx = map(int, input().split())
X = [list(input()) for _ in range(Hx)]
INF = 100

def search_corner(X):
    for h, line in enumerate(X):
        for w, c in enumerate(line):
            if c == "#":
                return h, w
    raise Exception

mha, mwa = search_corner(A)
mhb, mwb = search_corner(B)

cand = []
for h in range(Hx):
    for w in range(Wx):
        if X[h][w] == "#":
            cand.append((h, w))

for sha, swa in cand:
    for shb, swb in cand:
        Y = [["." for _ in range(Wx)] for _ in range(Hx)]
        flag = True
        for h in range(Ha): #, line in enumerate(A):
            for w in range(Wa):#, c in enumerate(line):
                if A[h][w] == "#":
                    hn = sha + (h - mha)
                    wn = swa + (w - mwa)
                    if 0 <= hn < Hx and 0 <= wn < Wx:
                        Y[hn][wn] = "#"
                    else:
                        flag = False
                        break

        for h, line in enumerate(B):
            for w, c in enumerate(line):
                if c == "#":
                    hn = h + (shb - mhb)
                    wn = w + (swb - mwb)
                    if 0 <= hn < Hx and 0 <= wn < Wx:
                        Y[hn][wn] = "#"
                    else:
                        flag = False
                        break
        if flag and Y == X:
            print("Yes")
            exit()
print("No")
