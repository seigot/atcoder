X = input()

#print(type(X))
#print(X[-1])        # 0
#print(X[-2])        # 5
#print(X[:len(X)])   # 50
#print(X[:len(X)-1]) # 5
#print(X[0:len(X)])  # 50
def myfloor(STR):
    ans = 0
    if 0 <= int(STR) < 10:
        # 1桁の正の数
        ans = 0
    elif -10 < int(STR) < 0:
        # 1桁の負の数
        ans = -1
    elif STR[-1] == '0':
        # (最後の桁が0の)2桁以上の数、floor関数を使った時に-1する必要がない
        ans = int(STR[:len(STR)-1])
    elif int(STR) > 0:
        # 2桁以上の正の数
        ans = int(STR[:len(STR)-1])
    else:
        # (最後の桁が0の)2桁以上の数、floor関数を使った時に-1する必要がある
        ans = int(STR[:len(STR)-1])-1

    return ans

print(myfloor(X))

print(myfloor(str(50)))
print(myfloor(str(234567)))
print(myfloor(str(-234567)))
print(myfloor(str(-(2**56))))
print(myfloor(str((2**56))))
