import sys
sys.setrecursionlimit(10**8)

N,T,M = map(int,input().split())
G = [set() for _ in range(N)]
for i in range(M):
  a,b = map(lambda x:int(x)-1,input().split())
  G[a].add(b)
  G[b].add(a)


def len_without_empty_set(l):
    num = 0
    for ii in range(len(l)):
        if l[ii]:
            num += 1
    return num

def dfs(v,res): # (人vを追加したい,現状の集合res)
  global ans
#  if v == N and res[T-1] and not res[T]: # N-1人追加済(v==N)かつ、チーム数がTの場合は解答+=1する
  if v == N and len_without_empty_set(res) == T:
    ans += 1
    return
  elif v == N: # N-1人追加済の場合は探索終了
    return

  # グループg(0~N)に人を追加することを考える
  for g in range(N):
    # 空のチームの場合は、グループを新設する
    if not res[g]:
      res[g].add(v)
      dfs(v+1,res)     # 人vをresに追加する
      res[g].remove(v) # 次の探索にはvは不要
      break
      
    # 既存のグループに追加する場合
    # 嫌いなペアがいるかどうかチェックして、いない場合は追加する
    flag = 1
    for v0 in res[g]: # 既に対象groupにいる人を全チェック
      if v in G[v0]:  # 既に対象groupにいる人(v0)が,追加しようとしている人vが嫌いな場合はflagOFF
        flag = 0
        break
    if flag:           # 誰も人vが嫌いではない場合、追加して探索する
      res[g].add(v)
      dfs(v+1,res)     # 人vをresに追加する
      res[g].remove(v) # 次の探索にはvは不要
      
ans = 0
dfs(0,[set() for _ in range(N+1)]) # (人0を追加したい,現状の集合)

print(ans)