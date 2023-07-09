l = list(map(str,input().split()))
hold = int(l[0])
nextl = l[1:]

ans = []
for st in nextl:
    S = int(st[0])
    ishold = st[1]
    if ishold == "y":
        ans.append(hold)
        hold = S
    else:
        ans.append(S)
print(*ans, sep="")

