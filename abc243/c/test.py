import sys
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
N=int(input())
l=[]
for i in range(N):
    l.append(list(map(int, input().split())))
S=input()

error(l)
error(S)

ll=[]
for i in range(N):
    #ll.append(l[i][0], l[i][1], S[i])
    error(l[i][0], l[i][1], S[i])
    ll.append([l[i][0], l[i][1], S[i]])

#sortfirst = lambda val: val[0]
#list = [[0, 2], [1, 1], [2, 0]]
#ll.sort(key=sortfirst)
ll.sort(key=lambda val: val[0])
sortsecond = lambda val: val[1]
#list = [[0, 2], [1, 1], [2, 0]]
ll.sort(key=sortsecond)

error(ll)

ans="No"
CurrentNo=-1
flag1=False
flag2=False
for i in range(N):
    # find R
    # find L
    if ll[i][1] != CurrentNo:
        CurrentNo = ll[i][1]
        flag1=False
        flag2=False
    if ll[i][2] == "R":
        flag1=True
    if ll[i][2] == "L" and flag1==True:
        flag2=True
        ans="Yes"

print(ans)
