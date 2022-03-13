
## python Tips

[過去問](https://github.com/seigot/atcoder/blob/main/doc/pastexam.md)

### header

```
import sys
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from collections import defaultdict
from bisect import bisect_right, bisect_left, insort_left, insort_right
```

### 標準入力

[初心者向けAtcoder標準入力セット(Python)](https://qiita.com/jamjamjam/items/e066b8c7bc85487c0785)

```
N=int(input())                     # (1)数字が1つ 入力例:N
A,B=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
S=input()                          # (3)文字列が1つ 入力例:S 
S,T=map(str, input().split())      # (4)文字列が2つ以上で別々に受け取り 入力例:S T
A=list(map(int, input().split()))  # (5)リストで受け取り 入力例:A1 A2 ... An
```

### テスト用の入力

```
cat in1.txt | python test.py
```

### よく使う機能

| 概要 |  処理  |  説明  |  備考  |
| ---- | ---- | ---- | ---- |
|  list操作  |  list  |  -  |  list = [] で初期化  |
|  -  |  list.append()  |  リストの最後にappend  |  -  |
|  -  |  list.pop(-1)  |  リストの最後をpop  |  -  |
|  -  |  list[::]  |  リストを出力  |  ['A', 'B', 'C']  |
|  -  |  list[::-1]  |  逆順で出力  |  ['C', 'B', 'A']  |
|  -  |  *list[::]  |  リストを出力(スペース区切りで)  |  A B C  |
|  -  |  *list[::-1]  |  逆順で出力(スペース区切りで)  |  C B A  |
|  文字列操作  |  String  |  -  |  S="xxx" で初期化  |
|  -  |  S[0]  |  文字列の最初の要素を出力  |  -  |
|  -  |  S[-1]  |  文字列の最後の要素を出力  |  -  |
|  -  |  S[::]  |  文字列を出力  |  ABC  |
|  -  |  S[::-1]  |  文字列を逆順で出力  |  CBA  |
|  集合  |  set  |  -  |  -  |
|  -  |  A & B  |  -  |  積集合  |
|  キュー  |  dequeue  |  -  |  -  |
|  変換  |  chr()  |  -  |  -  |
|  -  |  ord()  |  -  |  -  |
|  -  |  str()  |  -  |  -  |
|  -  |  int()  |  -  |  -  |
|  -  |  list()  |  -  |  -  |
|  演算子  |  //  |  floor関数  |  -  |

### 参考

[Pythonでリストをソートするsortとsortedの違い](https://note.nkmk.me/python-list-sort-sorted/)  
[２次元配列をソートした結果（昇順・降順・逆順） | Python](https://www.suzu6.net/posts/73-sort-2d-list/)  
[Pythonで最小公倍数、最大公約数を計算する](https://ictsr4.com/py/m0150.html)  
[AtCoder灰・茶・緑色の方必見！二分探索を絶対にバグらせないで書く方法](https://www.forcia.com/blog/001434.html)  
[Python defaultdict の使い方](https://qiita.com/xza/items/72a1b07fcf64d1f4bdb7)  
[Pythonのdequeでキュー、スタック、デック（両端キュー）を扱う](https://note.nkmk.me/python-collections-deque/)  
[Pythonで数字の桁数を取得する方法](https://qiita.com/RShirakawa/items/23f8f1d907dc40ebbdd2)
[Pythonの算術演算子（四則演算、べき乗、リスト・文字列の結合など）](https://note.nkmk.me/python-arithmetic-operator/)  
[pythonの内包表記を少し詳しく](https://qiita.com/y__sama/items/a2c458de97c4aa5a98e7)  
[数値と文字（文字列）を変換する (chr, ord, int, hex, oct, bin)](https://maku77.github.io/python/numstr/convert-number-and-string.html)
