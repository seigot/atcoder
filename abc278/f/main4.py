import sys
sys.setrecursionlimit(5*10**5)

n = int(input())
s = [input() for i in range(n)]

memo = dict()

def siri(use, last):
    # (これまでの探索済のbit列, 最新の探索対象文字列のindex)
  ans = 1

  if (use,last) in memo:
    return memo[(use, last)]

  # n bitを探索する
  for i in range(n):
    # 過去に探索したもの(use)のうち、既に探索済みの場合はスキップ
    if (use >> i) & 1:
        continue
    # 該当bitが未探索の場合は探索を試みる
    if last == -1 or s[last][-1] == s[i][0]:
      # lastが-1(最新)か
      # 最新の探索対象の末尾==現在の探索対象の先頭の場合は探索対象になる
      # (これまでの探索済のbit列+着目しているbit列, 最新の探索対象)
      ans &= siri(use + (1<<i), i)
      # 次につながるものが何もなかったら0を返す
      # --> 1つでも0が返るものがあれば1になるような仕組み

  ans ^= 1
  # おそらくansでFirst/Secondどちらがかつ状態かを管理している
  ## 0の場合: 全部1(繋がりがあるがどれも続きがある場合
  ## 1の場合: 繋がるものが何もない
  # 1つでも0になる場合は1にする、0になるケースが場合は0にする
  memo[(use, last)] = ans
  return ans

use = 0 # 00000000 nbit
print("First") if siri(use, -1) else print("Second")
