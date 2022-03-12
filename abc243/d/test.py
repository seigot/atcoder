import sys
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
N,X=map(int, input().split())
S=input()

#error(N,X)
#error(S)
#error(len(S))


SKIP=False
#SS=[0]*len(S)

SS=[]

# 前処理
for i in range(len(S)):
    if SKIP==True:
        SKIP=False
        continue
    elif S[i] != "U" and i+1<len(S) and S[i+1] == "U":
        SKIP=True
        continue
    else:
        SS.append(S[i])
error(SS)

ans=X
for i in range(len(SS)):
    if SS[i] == "U":
        ans = ans//2
    elif SS[i] == "L":
        ans = ans*2
    elif SS[i] == "R":
        ans = ans*2 +1
    else:
        pass

print(ans)

#    # first
#    if i==0 and S[i] == "U":
#        ans = ans//2
#        continue
#
#    # second, and after
#    if SKIP == True:
#        SKIP=False
#        continue
#    if S[i] == "L":
#        if i+1 < len(S) and S[i+1] == "U":
#            SKIP=True
#            continue
#        ans = ans*2
#    elif S[i] == "R":
#        if i+1 < len(S) and S[i+1] == "U":
#            SKIP=True
#            continue
#        ans = ans*2 +1
#

