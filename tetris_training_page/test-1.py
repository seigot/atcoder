l=list(map(int,input().split()))

minimum_val = min(l)
if l.count(minimum_val) == 1:
    if minimum_val == l[0]:
        print("Left")
    elif minimum_val == l[-1]:
        print("Right")
    else:
        print("NG")
else:
    print("NG")
