
## python Tips

[過去問](https://github.com/seigot/atcoder/blob/main/doc/pastexam.md)

### header

```
import sys
sys.setrecursionlimit(4100000)
import math
import itertools
import collections
from heapq import heapify, heappop, heappush
from bisect import bisect, bisect_left, bisect_right
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")
```

### 標準入力

[初心者向けAtcoder標準入力セット(Python)](https://qiita.com/jamjamjam/items/e066b8c7bc85487c0785)

```
N=int(input())                     # (1)数字が1つ 入力例:N
```

```
A,B=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
```

```
S=input()                          # (3)文字列が1つ 入力例:S 
```

```
S,T=map(str, input().split())      # (4)文字列が2つ以上で別々に受け取り 入力例:S T
```

```
A=list(map(int, input().split()))  # (5)リストで受け取り 入力例:A1 A2 ... An
```

```
A = deque(map(int, input().split()))  # (6)dequeueで受け取り 入力例:A1 A2 ... An
```

### テスト用の入力

```
cat in1.txt | python test.py
```
[Macから`atcoder-cli`を使った際の備忘録](https://qiita.com/seigot/items/ce9433e62bd2eea5a9ef)  

### よく使う機能

| 概要 |  処理  |  説明  |  備考  |
| ---- | ---- | ---- | ---- |
|  list操作  |  list  |  -  |  list = [] で初期化、(1次元配列の場合は`list = [0]*10`で初期化)  |
|  -  |  -  |  空のN次元配列  |  `l=[[] for i in range(N)]`  |
|  -  |  list[0]  |  リストの先頭の要素を出力  |  -  |
|  -  |  list[-1]  |  リストの終端の要素を出力  |  -  |
|  -  |  list.append()  |  リストの最後にappend  |  -  |
|  -  |  list.pop(-1)  |  リストの最後をpop  |  計算量はO(N) [参考](https://qiita.com/bee2/items/4ab87d05cc03d53e19f9)  |
|  -  |  list.pop(0)  |  リストの先頭をpop  |  -  |
|  -  |  list.sort()  |  リストをsortする  |  元のリスト自体が書き換えられる  |
|  -  |  -  |  (0番目の要素をキーとする場合)  |  list.sort(key=lambda val: val[0])  |
|  -  |  -  |  (1番目の要素をキーとする場合)  |  list.sort(key=lambda val: val[1])  |
|  -  |  -  |  (降順にsortしたい場合)  |  list.sort(reverse=True)  |
|  -  |  list[::]  |  リストを出力  |  ['A', 'B', 'C']  |
|  -  |  list[::-1]  |  逆順で出力  |  ['C', 'B', 'A']  |
|  -  |  *list[::]  |  リストを出力(スペース区切りで)  |  A B C  |
|  -  |  *list[::-1]  |  逆順で出力(スペース区切りで)  |  C B A  |
|  -  |  N次元配列(appendで要素追加)  |  内包表記  |  `l = [[] for _ in range(N)]`  |
|  辞書操作 | dict | - | `dict1 = {'X': 2, 'Y': 3, 'Z': 4}`で初期化 |
|  -  | defaultdict | | `d = defaultdict(int)` |
|  -  | 要素`'x'`を取り出して削除する | - | `d.pop('x')` |
|  -  | 要素`'x'`を取り出して削除する | - | `del d['x']` |
|  文字列操作  |  String  |  -  |  S="xxx" で初期化  |
|  -  |  S[0]  |  文字列の最初の要素を出力  |  -  |
|  -  |  S[-1]  |  文字列の最後の要素を出力  |  -  |
|  -  |  S[::]  |  文字列を出力  |  ABC  |
|  -  |  S[::-1]  |  文字列を逆順で出力  |  CBA  |
|  -  |  S[0:1]  |  文字列の1〜2文字目を出力  |  AB  |
|  -  |  S[1:]  |  文字列の2文字目以降を出力  |  BC, `[-2:]`で終端から2番目以降を出力  |
|  -  |  S[:1]  |  文字列の2文字目までを出力  |  AB  |
|  集合  |  set  |  -  |  初期化:`s = set()`  |
|  -  |  A & B  |  -  |  積集合  |
|  -  |  追加  |  -  |  `s.add('a')`  |
|  -  |  削除  |  (対象の要素がない場合はエラーになる)  |  `s.remove('a')`  |
|  -  |  削除  |  (対象の要素がない場合でもエラーにならない)  |  `s.discard('a')`  |
|  -  |  削除  |  (ランダムに要素を取り除く)  |  `s.pop()`  |
|  -  |  要素をforで回す  |  -  |  `for j in s:`  |
|  -  |  最小値を返す  |  -  |  `min(s)`  |
|  -  |  最大値を返す  |  -  |  `max(s)`  |
|  計数  |  Counter  |  listの要素をカウント(辞書型)  |  `from collections import Counter`、`c = Counter(l)` |
|  キュー  |  dequeue  |  -  |  `d = deque(['a', 'b', 'c'])`で初期化  |
|  - |  dequeue.append()  |  キューの右端にappend  |  -  |
|  - |  dequeue.appendleft()  |  キューの左端にappend  |  -  |
|  - |  dequeue.pop()  |  キューの右端をpop  |  -  |
|  - |  dequeue.popleft()  |  キューの左端をpop  |  -  |
|  -  |  heapq  |  優先度付きキュー  |  `from heapq import heappop, heappush` |
|  -  |  -  |  heapq.heapify(A)  |  リスト(A)を`heapq.heapify(A)`で優先度付きキューに変換  |
|  -  |  -  |  heapq.heappop(A)  |  heapqをPop(heapify(A)がないと初回先頭がpopされる)  |
|  -  |  -  |  heapq.heappush(A, N)  |  Push  |
|  -  |  -  |  -  |  タプル()は先頭要素基準でソートされる  |
|  変換  |  chr()  |  ascii-->charに変換  |  -  |
|  -  |  ord()  |  char-->asciiに変換  |  -  |
|  -  |  str()  |  文字列に変換  |  -  |
|  -  |  int()  |  整数に変換  |  -  |
|  -  |  float()  |  float型に変換  |  `is_integer()`で整数判定  |
|  -  |  list()  |  listに変換  |  -  |
|  -  |  set()  |  setに変換  |  -  |
|  演算子  |  **  |  べき乗  |  10の18乗(=`inf = 10**18`)  |
|  -  |  math.sqrt()  |  ルート  |  `import math`  |
|  -  |  //  |  floor関数(整数除算)  |  -  |
|  -  |  %  |  余り  |  -  |
|  -  |  divmod(N, M)  |  `N÷Mの`商と余りを返す  | `ans = divmod(10, 3) # ans[0]=3, ans[1]=1)`,<br> `q, mod = divmod(10, 3) # q=3, mod=1)`  |
|  -  |  +=  |  足し算  |  ex. a+=1(++は使えない)  |
|  -  |  -=  |  引き算  |  ex. a-=1(--は使えない)  |  
|  -  |  無限大(プラス方向)  |  `float`による表現([参考](https://note.nkmk.me/python-inf-usage/))  |  `inf = float('inf')`  |  
|  -  |  無限大(マイナス方向)  |  `float`による表現([参考](https://note.nkmk.me/python-inf-usage/))  |  `minf = -float('inf')`  |  
|  関数(補間)  |  comb()  |  コンビネーション  |  [comb.py](https://github.com/seigot/tools/blob/master/atcoder/comb.py)  |
|  木  |  multiset  |  データの挿入、削除、最大最小値取得などに便利な木  |  pythonにはデフォルトでの実装がない。C++の`<set>`を使うか自作が必要  |
|  その他  |  exit(0)  |  正常終了  |  -  |
|  -  |  while True:  |  無限ループ  |  -  |
|  -  |  最大公約数  |  a.bの最大公約数は、`math.gcd(a,b)`で取得する  |  [参考](https://note.nkmk.me/python-gcd-lcm/)  |
|  -  |  最小公倍数  |  a.bの最小公倍数は、`a*b//math.gcd(a,b)`で取得する  |  `math.lcm()`は、Python3.9で対応[参考](https://note.nkmk.me/python-gcd-lcm/)  |
|  -  |  等差数列の和  |  初項a,公差d,項数n,末項lにより求める  |  等差数列の和=`(a+l)n//2`,[参考](https://www.kwansei.ac.jp/hs/z90010/sugakua/suuretu/tousasum/tousasum.htm)  |



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
[2点間-最短経路アルゴリズム Showcase](https://qiita.com/gamita/items/9e2df8cfa1a7448aca53)
