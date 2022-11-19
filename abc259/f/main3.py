"""2022.07.09 20:55:52 JST"""
import sys
from functools import partial, reduce, lru_cache
from itertools import groupby, islice, tee, accumulate


def main():

    # 深さ優先探索
    def dfs(u, p):
        # 最初 u=0, p=-1
        m1 = 0

        # エッジの重み
        L = []
        for v, w in G[u]:
            # 頂点uに繋がっている辺とその重み
            if v == p:
                # 探索元が同じであればskip
                continue
            dfs(v, u)
            # 対象の辺のDが0以外であれば重みを追加する
            # 0であれば
            if D[v] != 0:
                L.append(dp[v][-2] - dp[v][-1] + w)
            else:
                L.append(0)
            m1 += dp[v][-1]

        # 探索
        L.sort(reverse=True)
        La = [0]
        for i in range(len(L)):
            # 累積和のようなもの
            La.append(max(La[-1] + L[i], La[-1]))

        dp[u][0] = m1
        for i in range(1, min(D[u] + 1, len(La))):
            dp[u][i] = max(m1 + La[i], dp[u][i - 1])
        for i in range(1, D[u] + 1):
            dp[u][i] = max(dp[u][i - 1], dp[u][i])

    N = int(readline())
    D = list(map(int, readline().split()))
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b, w = map(int, readline().split())
        G[a - 1].append((b - 1, w))
        G[b - 1].append((a - 1, w))
    # DP用の配列を用意する
    dp = []
    for i in range(N):
        dp.append([0] * (D[i] + 1))

    # 0番目の頂点を起点にする
    dfs(0, -1)
    #print(dp)
    print(max(dp[0]))


# @formatter:off
"+-+-+-+ Constants +-+-+-+"
MOD = 10 ** 9 + 7
# MOD = 998_244_353
INF = (1 << 62) - 1
"+-+-+-+ Settings +-+-+-+"
sys.setrecursionlimit(10 ** 6)
if "pypyjit" in sys.builtin_module_names:import pypyjit;pypyjit.set_param("max_unroll_recursion=-1");
use_buffer_read = False
"+-+-+-+ Libraries +-+-+-+"
# paste libraries here

"+-+-+-+ Memorize +-+-+-+"
_imm={}
"+-+-+-+ Print +-+-+-+"
printd=partial(print,file=sys.stderr)
printns=partial(print,sep='')
printl=partial(print,sep='\n')
"+-+-+-+ Math +-+-+-+"
aseq_sum1=lambda a1,d,n:n*(2*a1+(n-1)*d)//2
aseq_sum2=lambda a1,an,n:n*(a1+an)//2
aseq_msum1=lambda a1,d,n:(n*(2*a1+(n-1)*d)*invmod(2))%MOD
aseq_msum2=lambda a1,an,n:(n*(a1+an)*invmod(2)) % MOD
gseq_sum=lambda a,r,n:a*(pow(r,n)-1)//(r-1) if r!=1 else a*n
gseq_msum=lambda a,r,n:a*(pow(r,n,MOD)-1)*invmod(r-1)%MOD if r!=1 else a*n%MOD
divceil=lambda x,y:(x+y-1)//y
invmod=lambda x:_imm.setdefault(x,pow(x,MOD-2,MOD))
"+-+-+-+ Iter +-+-+-+"
crange=lambda *args:range(args[0]+1) if len(args)==1 else range(args[0],args[1]+1,1 if len(args)==2 else args[2])
rrange=lambda *args:reversed(range(*args))
"+-+-+-+ List +-+-+-+"
cst2l=lambda first,second,initial=0:[[initial]*second for _ in range(first)]
copy2l=lambda L:[r[:] for r in L]
"+-+-+-+ String +-+-+-+"
concat=lambda L,sep='':sep.join(L)
ston=lambda S,a=0:[(ord(c)|32)-(97-a) for c in S]
"+-+-+-+ Algorithms +-+-+-+"
ccomp=lambda A:{x:i for i,x in enumerate(sorted(set(A)))}
invert=lambda A,start=0:dict(zip(A,range(start,len(A)+start)))
lpartion = lambda L,b:[L[i:i+b] for i in range(0,len(L),b)]
nwise=lambda n,A:zip(*(islice(it,s,None) for it,s in zip(tee(A,n),range(n))))
runlength=lambda A:[[k,len(list(g))] for k,g in groupby(A)]
__c1=0x5555555555555555;__c2=0x3333333333333333;__c3=0xf0f0f0f0f0f0f0f;__c4=0xff00ff00ff00ff;__c5=0xffff0000ffff;__c6=0xffffffff;
def popcount(n):c=(n&__c1)+((n>>1)&__c1);c=(c&__c2)+((c>>2)&__c2);c=(c&__c3)+((c>>4)&__c3);c=(c&__c4)+((c>>8)&__c4);c=(c&__c5)+((c>>16)&__c5);c=(c&__c6)+((c>>32)&__c6);return c
"+-+-+-+ Read +-+-+-+"
__file=open(0)
read=__file.buffer.read if use_buffer_read else __file.read
readline=__file.buffer.readline if use_buffer_read else __file.readline
readlines=__file.buffer.readlines if use_buffer_read else __file.readlines
"+-+-+-+ Run +-+-+-+"
main()
# @formatter:on

