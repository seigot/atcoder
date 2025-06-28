
## python Tips

[過去問](https://github.com/seigot/atcoder/blob/main/doc/pastexam.md)

### header

```
#!/usr/bin/env python3                                                                                                                                                                                                                              
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(4100000)
import math
import os
from inspect import currentframe
ONLINE_JUDGE = os.environ["HOME"] == "/home/runner"
def error1(*args, end="\n"): # 変数のみ表示
    if ONLINE_JUDGE: return
    print("[stderr]", *args, end=end, file=sys.stderr)
def error(*args): # 変数の名前と値をまとめて表示
    if ONLINE_JUDGE: return
    names = {id(v): k for k, v in currentframe().f_back.f_locals.items()}
    print("[stderr]",' '.join([names.get(id(arg), '???') + ' = ' + repr(arg) for arg in args]), file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from math import gcd
from itertools import permutations,combinations,accumulate
from copy import deepcopy
dpos2 = ((1, 0), (0, 1))
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos4cross = ((1, 1), (1, -1), (-1, 1), (-1, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
MOD = 998244353
def invmod(a): # 期待値の計算: X/Y % MOD = X * invmod(Y) % MOD
    return pow(a,-1,MOD)
def conv_2dto1d(h, w, W): # h:height, w:width, W:横幅
    return h * W + w
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

```
from decimal import Decimal
AB=[list(map(Decimal, input().split())) for _ in range(N)] # decimal(小数の誤差を正確に扱う)使う場合はpython3にする(pypyだと遅い)
```

```
maze = [list(input()) for h in range(H)] # maze(###.###) のようなスペースなしの2次元配列で受け取り
P=[list(map(int, input().split())) for h in range(H)] # 1 2 3 4 のようなスペースありの2次元配列を受け取り
```

### 変数の宣言

```
# graph (N頂点M辺)
N,M=map(int, input().split())
gh = [[] for _ in range(N)] 
for ii in range(M):
    u,v=map(int, input().split())
    u -= 1  # 0-indexの場合/1-indexの場合は不要
    v -= 1  # 0-indexの場合/1-indexの場合は不要
    gh[u].append(v)
    gh[v].append(u)
```

```
# 2次元配列 ( (10**5)*(10**5)のようなサイズは宣言時にエラーになるので注意 )
dp = [[0]*(n+1) for _ in range(n+1)]
## defaultdictを使う場合
dp = [defaultdict(int) for _ in range(n+1)]
# 3次元配列
dp = [[[0]*(n+1) for _ in range(n+1)] for _ in range(n+1)]
```

### テスト用の入力

```
cat in1.txt | python test.py
```

でもテスト用の入力は結局コピペが便利な気もする..

### `atcoder-cli`
[Macから`atcoder-cli`を使った際の備忘録](https://qiita.com/seigot/items/ce9433e62bd2eea5a9ef)  

### vscodeスニペット

[VS Codeのユーザースニペット機能の使い方メモ](https://qiita.com/12345/items/97ba616d530b4f692c97)
> スニペットは定形のテキストをあらかじめ登録しておいてそれを呼び出す機能(他のツールだと「テンプレート」「雛型」みたいな言い方もする)。あらかじめ定義されているスニペットを利用する以外に、自分でスニペットを定義することもできる(ユーザースニペット)。
ソースコードでも文章でも、普段の作業でよく入力するテキストを登録しておけば作業のスピードアップになるし入力間違いを防ぐこともでき、使い方によって作業効率がかなり上がる。

未(以下をスニペットにしたい)
- グラフ
- 幅優先探索,dijkstra
- unionfind
etc  

### よく使う機能

| 概要 |  処理  |  説明  |  備考  |
| ---- | ---- | ---- | ---- |
|  list操作  |  list  |  -  |  list = [] で初期化、(1次元配列の場合は`list = [0]*10`で初期化)  |
|  -  |  -  |  空のN次元配列  |  `l=[[] for i in range(N)]`  |
|  -  |  -  |  0初期化の2次元配列(H行 * W列)  |  `l=[[0 for i in range(W)] for j in range(H)]`  |
|  -  |  list[0]  |  リストの先頭の要素を出力  |  -  |
|  -  |  list[-1]  |  リストの終端の要素を出力  |  -  |
|  -  |  list[1:]  |  リストの1番目以降の要素を出力  |  -  |
|  -  |  list.append()  |  リストの最後にappend  |  -  |
|  -  |  list.pop(-1)  |  リストの最後をpop  |  計算量はO(1),(通常はO(N)かかるが最後をpopする場合はO(1) [参考](https://qiita.com/bee2/items/4ab87d05cc03d53e19f9), `list.pop()`と同じ  |
|  -  |  list.pop(0)  |  リストの先頭をpop  |  -  |
|  -  |  list.index(N)  |  リストの要素のうちNのindexを返す  |  -  |
|  -  |  list.remove("a")  |  リストの要素を1つ削除(左記は"a"を削除)  |  `ex.) list.remove("a"),list.remove(10)` |
|  -  |  list.sort()  |  リストをsortする  |  元のリスト自体が書き換えられる  |
|  -  |  -  |  (0番目の要素をキーとする場合)  |  list.sort(key=lambda val: val[0])  |
|  -  |  -  |  (1番目の要素をキーとする場合)  |  list.sort(key=lambda val: val[1])  |
|  -  |  -  |  (降順にsortしたい場合)  |  list.sort(reverse=True)  |
|  -  |  list[::]  |  リストを出力  |  ['A', 'B', 'C']  |
|  -  |  list[::-1]  |  逆順で出力  |  ['C', 'B', 'A']  |
|  -  |  *list[::]  |  リストを出力(スペース区切りで)  |  A B C、`print(*list, sep='\n')のようにsepも設定できる`  |
|  -  |  *list[::-1]  |  逆順で出力(スペース区切りで)  |  C B A  |
|  -  |  N次元配列(appendで要素追加)  |  内包表記  |  `l = [[] for _ in range(N)]`  |
|  -  |  2次元配列(0初期化)  |  内包表記  |  `d = [[0] * n for _ in range(n)]`  |
|  -  |  if文ありの内包表記  |  内包表記  |  `comprehension_2 = [i for i in range(10) if i%2==0]`, [ifを含む場合後置if)](https://qiita.com/y__sama/items/a2c458de97c4aa5a98e7#ifを含む場合後置if)  |
|  -  |  listのindex,値をどちらも取得したい  |  `enumerate()`  |  `for i,a in enumerate(A): print(i,a)`  |
|  辞書操作 | dict | - | `dict1 = {'X': 2, 'Y': 3, 'Z': 4}`で初期化 |
|  -  | defaultdict(default 0) | | `d = defaultdict(int)` |
|  -  | defaultdict(default -1) | | `d = defaultdict(lambda:-1)` |
|  -  | defaultdict(default INF) | | `d = defaultdict(lambda: 10**10)` |
|  -  | defaultdict(default list) | | `d = defaultdict(list)`で初期化、`d[x].append(y)`で値を加える |
|  -  | defaultdict(default set) | | `d = defaultdict(set)`で初期化、`d[x].add(y)`で値を加える |
|  -  | defaultdictの要素を取得 | `d.keys():` | dictの要素をループさせる. `for ii in d.keys():`... |
|  -  | defaultdictの最大のindexを取得 | `max(d)` | - |
|  -  | defaultdictの最大のindex(key)を取得 | `max(d.keys())` | (値が0のものも数える。数えたくない場合は`del d[x]`等で消しておく) |
|  -  | defaultdictのkeys,valuesを取得 | `d.items()`,`for k,v in d.items():` | - |
|  -  | defaultdictの最大値を取得 | `max(d.values())` | - |
|  -  | 要素`'x'`を取り出して削除する | - | `d.pop('x')` |
|  -  | 要素`'x'`を取り出して削除する | - | `del d['x']` |
|  -  | `Counter() (collectionsの中にある辞書型)`、 | - | `from collections import Counter` `d = Counter()` |
|  文字列操作  |  String  |  -  |  S="xxx" で初期化  |
|  -  |  S[0]  |  文字列の最初の要素を出力  |  -  |
|  -  |  S[-1]  |  文字列の最後の要素を出力  |  -  |
|  -  |  S[::]  |  文字列を出力  |  ABC  |
|  -  |  S[::-1]  |  文字列を逆順で出力  |  CBA  |
|  -  |  S[0:2]  |  文字列の0-1番目（1〜2文字目）を出力  |  AB  |
|  -  |  S[:2]  |  文字列の1番目まで（2文字目まで）を出力  |  AB  |
|  -  |  S[1:]  |  文字列の1番目（2文字目以降）を出力  |  BC, `[-2:]`で終端から2番目以降を出力  |
|  -  |  S.replace(org,mod)  |  文字列を置換して結果を返す  |  `s = s.replace("eraser", "-")`  |
|  -  |  S.find()  |  文字列を検索してインデックスを返す(前から検索)  |  `s = s.find("eraser")`  |
|  -  |  S.find()  |  文字列を検索してインデックスを返す(後ろから検索)  |  `s = s.rfind("eraser")`  |
|  -  |  S.split("abc")  |  文字列"abc"を基準にSを分割する  |  `s = s.split("abc")`  |
|  -  |  S.upper()  |  文字列を小文字から大文字に変換  |  `s = s.upper() # s = "abc" --> "ABC"`  |
|  -  |  S.lowwer()  |  文字列を大文字から小文字に変換  |  `s = s.lower() # s = "ABC" --> "abc"`  |
|  -  |  文字列の改行判定 |  文字列が改行コード`\n`かどうか判定する  |  `if S[i] == "\n": continue`  |
|  集合  |  set  |  注意：pythonのsetの表示される順番は保証されない   |  初期化:`s = set()` |
|  -  |  和集合  |  (A or B)  |  s = s1 &#124; s2  |
|  -  |  積集合  |  (A and B)  |  `s = s1 & s2`  |
|  -  |  追加  |  -  |  `s.add('a')`  |
|  -  |  (集合を追加)  |  -  |  `s.update(s2)`, (`s.union()は遅いので非推奨`)  |
|  -  |  (集合を追加)  |  -  |  `S1.add for ii in S2`, (`S2をS1にfor文で追加していく。サイズの小さい方-->大きい方にマージするとO(logN)になるらしい`)  |
|  -  |  削除  |  -  |  `s.clear()`  |
|  -  |  ~~一時的な追加（コピー）~~  |  ~~deepcopyを使う(単純なコピーだと参照渡しになる模様..)~~  |  ~~`array2 = copy.deepcopy(array)`~~  |
|  -  |  一時的な追加（コピー）  |  deepcopyよりスライスを使った方が速い  | array2 ` = array[:]`  |
|  -  |  一時的な追加（コピー）  |  "&#124;"を使う  |  `tmp_used = used` &#124; `{(ni,nj)}`  |
|  -  |  削除  |  (対象の要素がない場合はエラーになる)  |  `s.remove('a')`  |
|  -  |  削除  |  (対象の要素がない場合でもエラーにならない)  |  `s.discard('a')`  |
|  -  |  削除  |  (ランダムに要素を取り除く)  |  `s.pop()`  |
|  -  |  要素をforで回す  |  -  |  `for j in s:`  |
|  -  |  最小値を返す  |  -  |  `min(s)`  |
|  -  |  最大値を返す  |  -  |  `max(s)`  |
|  -  |  setのsort  |  -  |  組込み関数`sorted`を使う, `sorted_set = sorted(passed_exam_idx)`  |
|  -  |  集合同士の比較  |  -  |  同じ集合であることを数えるには`s1 == s2`でOK  |
|  -  |  集合同士の比較  |  -  |  集合の部分集合/超集合を比較するには`s.issubset(s2)`,` s.issuperset(s2)`を使う  |
|  -  |  空集合かどうか判定  |  集合の部分集合/超集合を比較  | 空集合ではない場合`if s: print("not empty_set")`, 空集合の場合`if not s: print("empty_set")`  |
|  計数  |  Counter  |  listの要素をカウント(辞書型)  |  `from collections import Counter`、`c = Counter(l)` |
|  キュー  |  dequeue  |  -  |  `d = deque(['a', 'b', 'c'])`で初期化,[配列アクセスの計算量はO(N)](https://qiita.com/snhrhdt/items/2e514d4d6af983fcf6f0)  |
|  - |  dequeue.append()  |  キューの右端にappend  |  -  |
|  - |  dequeue.appendleft()  |  キューの左端にappend  |  -  |
|  - |  dequeue.pop()  |  キューの右端をpop  |  -  |
|  - |  dequeue.popleft()  |  キューの左端をpop  |  -  |
|  -  |  heapq  |  優先度付きキュー  |  `from heapq import heappop, heappush` |
|  -  |  -  |  heapq.heapify(A)  |  リスト(A)を`heapq.heapify(A)`で優先度付きキューに変換  |
|  -  |  -  |  heapq.heappop(A)  |  heapqをPop(heapify(A)がないと初回先頭がpopされる)  |
|  -  |  -  |  heapq.heappush(A, N)  |  Push  |
|  -  |  -  |  -  |  タプル()は先頭要素基準でソートされる  |
|  変換  |  chr()  |  ascii-->charに変換  |  `chr(ord("A")+1)-->B`  |
|  -  |  ord()  |  char-->asciiに変換  |  `ord("A")-->65`   |
|  -  |  str()  |  文字列に変換  |  -  |
|  -  |  int()  |  整数に変換  |  -  |
|  -  |  float()  |  float型に変換  |  `is_integer()`で整数判定, `float(c).is_integer() == True #整数である場合`  |
|  -  |  list()  |  listに変換  |  -  |
|  -  |  set()  |  setに変換  |  -  |
|  演算子  |  **  |  べき乗  |  10の18乗(=`inf = 10**18`), powの方が高速  |
|  -  |  pow()  |  べき乗  |  `pow(x, y, z) は pow(x, y) % z`という意味  |
|  -  |  pow()  |  逆数を求めることも可能(mの逆数をmodで割ったものを求める場合)  |  mod = 998244353<br>minv = pow(m, mod-2, mod)<br>#(python3.8以降の場合)minv = pow(m, -1, mod)  |
|  -  |  math.sqrt()  |  ルート  |  `import math`,`n**0.5`でもOK  |
|  -  |  //  |  floor関数(整数除算)  |  `math.floor`だと精度足りない場合があるかも  |
|  -  |  math.ceil()  |  切り上げ   |  -  |
|  -  |  %  |  余り  |  `a %= b` (`a = a%b` は遅い)  |
|  -  |  divmod(N, M)  |  `N÷Mの`商と余りを返す  | `ans = divmod(10, 3) # ans[0]=3, ans[1]=1)`,<br> `q, mod = divmod(10, 3) # q=3, mod=1)`  |
|  -  |  +=  |  足し算  |  ex. a+=1(++は使えない)  |
|  -  |  -=  |  引き算  |  ex. a-=1(--は使えない)  |  
|  -  |  無限大(プラス方向)  |  `float`による表現([参考](https://note.nkmk.me/python-inf-usage/))  |  `inf = float('inf')`  |  
|  -  |  無限大(マイナス方向)  |  `float`による表現([参考](https://note.nkmk.me/python-inf-usage/))  |  `minf = -float('inf')`  |  
|  -  |  ビット演算(&)  |  AND  |    |
|  -  |  ビット演算(&#124;)  |  OR  |    |
|  -  |  ビット演算(^)  |  xor  |  [Pythonのビット演算子](https://note.nkmk.me/python-bit-operation/)  |
|  -  |  ビット演算(^)  |  xorを使って0,1を反転する  |  `print(1^1)-->0`,`print(0^1)-->1`  |
|  -  |  ビット演算(~)  |  not  |    |
|  -  |  ビット演算(<<, >>)  |  シフト  |    |
|  -  |  2進数表記(0bxxx)  |  -  |  `2進数、8進数、16進数、= 0b, 0o, 0x`  |
|  定数  |  math.pi  |  π  |  角度(°)から弧度(rad)への変換式:`rad=theta*math.pi/180`  |
|  -  |  逆元  |  [逆元](https://qiita.com/drken/items/3b4fdf0a78e7a138cd9a)  |  `modinv = lambda x:pow(x, -1, MOD) # 逆元を求める。python3.8であればOK` #   |
|  -  |  -  |  -  |  `modinv = lambda x:pow(x, MOD - 2, MOD) # 逆元を求める。pypyの場合はこちらを使う`#   |
|  関数(補間)  |  comb()  |  コンビネーション  |  [comb.py](https://github.com/seigot/tools/blob/master/atcoder/comb.py)  |
|  その他  |  exit(0)  |  正常終了  |  -  |
|  -  |  print()  |  配列内の文字列を結合して表示（map利用）  |  `ans = [1]*10000000`<br>`print("".join(list(map(str, ans))))` |
|  -  |  print()  |  配列内の文字列を結合して表示（基本的に文字列を扱うよりも速度が早いはず）  |  `ans = [1]*10000000`<br>`print("".join(ans))` |
|  -  |  print()  |  少数けた表示  |  ex.10位まで表示 `print('{:.10f}'.format(ans))` |
|  -  |  print()  |  if/elseを1行で書く少数けた表示  |  `print('Yes' if ans==1 else 'No')` |
|  -  |  print()  |  flush  |  `print(node, flush=True)` |
|  -  |  True:  |  無限ループ  |  -  |
|  -  |  for i in xxx:  |  文字列のループ  |  `base="ABCDEFGHIJKLMNOPQRSTUVWXYZ"`<br> `for i in base:`<br>`print(i)` |
|  -  |  for ii in range(10):  |  ループ(昇順)  |  -  |
|  -  |  for ii in range(10)[::-1]::  |  ループ(降順)  |  -  |
|  -  |  最大公約数  |  a.bの最大公約数は、`math.gcd(a,b)`で取得する(※python3.8だと、2つのgcd(a,b)のみ対応している)  |  [参考](https://note.nkmk.me/python-gcd-lcm/)  |
|  -  |  最小公倍数  |  a.bの最小公倍数は、`a*b//math.gcd(a,b)`で取得する  |  `math.lcm()`は、Python3.9で対応[参考](https://note.nkmk.me/python-gcd-lcm/)  |
|  -  |  約数列挙  |  約数をlist形式で取得する()  |  [約数を高速で列挙するコード(Python)](https://qiita.com/LorseKudos/items/9eb560494862c8b4eb56#%E3%82%B3%E3%83%BC%E3%83%89)<br>`l = make_divisors(K)`<br>`#print(l) # [1, 2, 3, 4, 6, 12]`  |
|  -  |  等差数列の和  |  初項a,公差d,項数n,末項lにより求める  |  等差数列の和=`(a+l)n//2`,[参考](https://www.kwansei.ac.jp/hs/z90010/sugakua/suuretu/tousasum/tousasum.htm)  |
|  -  |  連番の取得  |  rangeをlist()する  |  `print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`  |
|  -  |  内積と外積  |  内積:xxx、外積:ベクトルを用いて符号付面積を求める(180度以上かどうかで正負別れる)  |  [リンク](http://marupeke296.com/COL_Basic_No1_InnerAndOuterProduct.html)  |
|  -  |  permutations  |  文字列の全探索する場合は`permutations`が便利  |  -  |
|  -  |  print(flushする場合)  |  `print(m, flush = True)` |  -  |


| 概要 |  処理  |  説明  |  備考  |  過去問  |
| ---- | ---- | ---- | ---- | ---- |
|  数  |  エラトステネスの篩  |  `N`以下の素数をすべて求めるためのアルゴリズム  |  [エラトステネスのふるいとは](https://algo-method.com/descriptions/64)  |  [typical90 030 K-Factors](https://atcoder.jp/contests/typical90/tasks/typical90_ad)  |
| 概要 |  処理  |  説明  |  備考  |  過去問  |
| ---- | ---- | ---- | ---- | ---- |
|  木  |  multiset  |  データの挿入、削除、最大最小値取得などに便利な木  |  pythonにはデフォルトでの実装がない。C++の`<set>`を使うか自作が必要 [参考](https://qiita.com/mymelochan/items/0c72d8b7ae8d9c3d836a)  |    |
|  -  |  根付き木  |  -  |  木DP  |  [木DP問題](https://atcoder.jp/contests/abc259/tasks/abc259_f)  |
|  -  |  -  |  木の直径  |  最大距離を二回求めると直径が求まる  |    |
|  -  |  -  |  木のサイズ  |  各頂点のサイズ（頂点の数）はDFSで求める  |    |
|  -  |  heap木  |  heapq 優先度付きキューから最小値を取り出す(O(logN))  |  dijkstra法で使う  |  [typical90 013 - Passing（★5）](https://atcoder.jp/contests/typical90/tasks/typical90_m)  |
|  -  |  セグメント木  |  区間に対する集約処理をするときによく使われる  |  [セグメント木](https://ikatakos.com/pot/programming_algorithm/data_structure/segment_tree)  |  [typical90 029 longbricks](https://atcoder.jp/contests/typical90/tasks/typical90_ac) [セグメント木の実装](https://atcoder.jp/contests/typical90/submissions/33896598)  |
|  探索  |  深さ優先探索  |  探索空間を深さ優先で探索する。再帰処理が便利、queも使える(?)  |  -  |  -  |
|  -  |  幅優先探索  |  探索空間を均等に探索する。`que`が便利。  |  -  |  -  |
|  -  |  いもす法   |  いもす法とは，累積和のアルゴリズムを多次元，多次数に拡張したものです  | [いもす法](https://imoz.jp/algorithms/imos_method.html) | [typical90 028 clutter paper](https://atcoder.jp/contests/typical90/tasks/typical90_ab) |
|  -  |  2分探索  |  グラフが単調増加する場合の境目を探索する  |  -  |  -  |
|  -  |  3分探索  |  グラフが凸である場合の極小（極大）を探索する  |  -  |  -  |
|  グラフ  |  頂点数に関する内包表記  |  -  |  `edges = [[] for _ in range(N)]`  |  -  |
|  -  |  union-find  |  同じ木に属しているかを判定するのに便利な木  |  uf = UnionFind(6),[PythonでのUnion-Find](https://note.nkmk.me/python-union-find/)  |  -  |
|  -  |  -  |  -  |  `uf.union(a,b)`: (a,b)を同じグループに所属させる.<br>`uf.same(a,b)`:(a,b)が同じグループかどうかを判定する.<br>`uf.same(a)`:aの属するグループのサイズを取得する  |  -  |
|  各種データ構造  |  sorted_set  |  要素の追加/要素の削除/x以上の最小の要素の検索をlog(N)で扱える凄いデータ構造 | [Python で std::set の代替物を作った](https://github.com/tatyam-prime/SortedSet), https://github.com/tatyam-prime/SortedSet  |  -  |

## `pypy`と`python`

| 項目 |  選択基準  |
| ---- | ---- |
|  pypy  |  基本的にはこちらを選択した方が良さそう(繰り返し処理など処理全般早い)  |
|  python  |  再帰関数を処理する場合はこちらが良さそう  |

[【競プロ】PythonとPyPyの速度比較](https://qiita.com/y-oksaku/items/f0c5c4681bc30dddf7f4)

## 方針

| 段階 |  -  |  -  |  基準  |
| ---- | ---- | ---- | ---- |
| 問題の意味がわかる |  |  |  |
| 計算量を見積もる | 全探索が可能かどうか,（`10**7`を超えるかどうか） |  |  |
| - | `10**7`を超える場合はlogN,NlogNに変換できないか） |  |  |
| 解き方の方針がわかる | 典型 | 全探索 |  |
| - | - | メモ化(辞書化して再利用) |  |
| - | - | 周期性(割り算の余り等) |  |
| - | - | 差分に着目 |  |
| - | - | O(1)の活用(set()) |  |
| - | 実験 |  |  |
| - | ググる(combinations等のライブラリ) |  |  |
| - | エスパー |  |  |
| 解き方の実装方針がわかる |  |  |  |
| - | 解法脳内simulationしてから実装 |  |  |
| 解き方の実装ができる |  |  |  |
| - | テスト/コーナケース |  |  |
| 解き方のデバッグができる | コーナーケース |  |  |
| - | 数値が大きいケース |  |  |
| - | 変数typo |  |  |
| - | 誤読 |  |  |
| 解き方の振り替えりができる |  |  |  |

## よくわからずに`WA`してしまった時

| 振り返り観点 |  内容  |  備考  |
| ---- | ---- | ---- |
| 問題文の見直し |  前提条件について何か足りていない点がないか  | - |
| 誤差 |  sqrt,割り算  | floatを扱わない方法を考える。sqrtは2乗のまま計算できないか、割り算を避けれないか、等。 |
| 誤差 |  modのタイミング  | 計算中のMOD/最後の出力前のMOD、等。 |
| コーナーケース |  極端に数値が小さい、大きい、条件の端  | 数WAの際に注意 |

### zip/enumerate

```
A = [1,2,3]
S = "abc"
for a, c in zip(A, S):
    print(a,c)
    # 1 a
    # 2 b
    # 3 c
```

```
for ii, a in enumerate(A):
    print(ii,a)
    # 0 1
    # 1 2
    # 2 3

for ii, s in enumerate(S):
    print(ii,s)
    # 0 a
    # 1 b
    # 2 c
```

### sort

組み込み関数`sorted()`を使う  
複数要素を配列に持たせる場合はkey指定の有無により挙動が変わる

```
# sort
a = [(1,9),(1,8),(1,10),(3,9),(3,8),(3,10),(2,9),(2,8),(2,10)]
print(sorted(a))                     # x満遍なくソート    [(1, 8), (1, 9), (1, 10), (2, 8), (2, 9), (2, 10), (3, 8), (3, 9), (3, 10)]
print(sorted(a, key=lambda x: x[0])) # 0番目の要素でソート [(1, 9), (1, 8), (1, 10), (2, 9), (2, 8), (2, 10), (3, 9), (3, 8), (3, 10)]
print(sorted(a, key=lambda x: x[1])) # 1番目の要素でソート [(1, 8), (3, 8), (2, 8), (1, 9), (3, 9), (2, 9), (1, 10), (3, 10), (2, 10)]

# 降順ソートしたい場合：
- "reverse=True"オプション付ける
- キーの数値を負にする
```

分数の誤差に影響されずソートしたい場合は`cmp_to_key`使う  
もしくはDecimalを使う

```
# https://qiita.com/nishizumi_noob/items/7a1323c45cf6ce56a368
from functools import cmp_to_key

def cmp(a, b):  # a = [x_a, y_a], b = [x_b / y_b]
    # 比較対象の分数 a と b が等しければ 0 を返す
    if a[0] * b[1] == b[0] * a[1]:
        return 0
    # a, bという順で並んでほしい条件のときは-1を返し、それ以外では1を返す
    return -1 if a[0] * b[1] < b[0] * a[1] else 1
    # 降順にしたい場合は、不等号をかえる
    #return -1 if a[0] * b[1] > b[0] * a[1] else 1

l = [[5, 7], [3, 8], [1, 2]]  # リストの各要素は [分子, 分母] とする
l = sorted(l, key=cmp_to_key(cmp))
print(l) # l = [[3, 8], [1, 2], [5, 7]]

from functools import cmp_to_key
def cmp(a, b):  # a = [x_a, y_a], b = [x_b / y_b]
    # 比較対象の分数 a と b が等しければ 0 を返す
    if a[0] * b[1] == b[0] * a[1]:
        ## [2]にidがある場合
        if len(a) == 3:
            if a[2] < b[2]:
                # 同じa,bにindexがある場合indexの小さい順に並び替える 
                return -1
        return 0
    # a, bという順で並んでほしい条件のときは-1を返し、それ以外では1を返す
    return -1 if a[0] * b[1] > b[0] * a[1] else 1
l = [[5, 7], [3, 8], [3, 8], [1, 2]]  # リストの各要素は [分子, 分母] とする
l = sorted(l, key=cmp_to_key(cmp))
print(l) # [5, 7], [1, 2], [3, 8], [3, 8]]
l = [[5, 7, 1], [3, 8, 3], [3, 8, 2], [1, 2, 4]]  # リストの各要素は [分子, 分母] とする
l = sorted(l, key=cmp_to_key(cmp))
print(l) # [[5, 7, 1], [1, 2, 4], [3, 8, 2], [3, 8, 3]]
```

### 集合

#### 部分集合/超集合を判定`issubset/issuperset`)

```
s = set([2,3,4,5])
s2 = set([2,3])
# s.issubset(s2)   : 部分集合
# s.issuperset(s2) : 超集合
print(s.issubset(s2))   # False
print(s.issuperset(s2)) # True
print(s2.issubset(s))   # True
print(s2.issuperset(s)) # False
print(s.issubset(s))    # True (同じ場合はTrue)
print(s.issuperset(s))  # True (同じ場合はTrue)
print(s < s2) # False (sはs2の部分集合である --> False)
print(s > s2) # True  (sはs2の超集合である --> True)
```

#### 空集合かどうかを判定

```
def test_is_empty_set(s):
    if s: print("not empty_set")
    if not s: print("empty_set")
s = set()
test_is_empty_set(s) # empty_set
s.add(1)
test_is_empty_set(s) # not empty_set
```

### 二次元配列探索時のindex

4方向

```
#       (-1,0)
# (0, -1)     (0, 1) 
#       (1,0)
dy = [-1, 0, 1,  0]
dx = [ 0, 1, 0, -1]
```

8方向

```
# (-1,-1) (-1,0) (-1, 1)
# (0, -1)        ( 0, 1) 
# (1, -1) (1,0)  ( 1, 1)
dy = [-1, -1, 0, 1, 1,  1 , 0  , -1]
dx = [ 0,  1, 1, 1, 0, -1 , -1 , -1]
```

### combinations

`M`個の要素のから`N`個を取り出す方を全て辞書順に出力する

```
from itertools import combinations
# print(*combinations(range(1, M+1), N))
print(*combinations(range(1, 10), 2))
```

### combinations_with_replacement

組合せ(重複あり)

```
from itertools import combinations_with_replacement
for k in combinations_with_replacement(range(3), 2):
    print(k)
#(0, 0)
#(0, 1)
#(0, 2)
#(1, 1)
#(1, 2)
#(2, 2)
```

### permutations

順列の取得
`M`個の要素のから`N`個を取り出す方を出力する、defaultは`M`個を取り出す

```
from itertools import permutations
for p in permutations(list(range(M))):
    print(p)    # ex.(0, 1, 2) if M=3
    print(p[0]) #     0
    print(p[1]) #     1
    print(p[2]) #     2
```

### permutations(next_permutationsの代わり)

重複なしの`next_permutations`をpythonで以下の通り代替する。  

```
# next_permutationの代わり
next_perm = ["".join(p) for p in permutations(S,len(S))]
next_perm.sort()
for kk in range(len(next_perm)):
    if kk > 0 and next_perm[kk-1] == next_perm[kk]:
        continue
    s = next_perm[kk]
    #...
```

### product

指定した配列の要素の組み合わせを出力

```
from itertools import product
R=list(map(int, input().split()))
# R = [2 1 3]

ll = [[] for _ in range(N)] 
# 配列を取得
for ii in range(N):
    ll[ii] = [x for x in range(1, R[ii] + 1)]
# ll = [[1, 2], [1], [1, 2, 3]]
for vv in product(*ll):
    print(vv)
    # それぞれの配列の要素の組み合わせを出力
    # vv = (1, 1, 1)
    # vv = (1, 1, 2)
    # vv = (1, 1, 3)
    # vv = (2, 1, 1)
    # vv = (2, 1, 2)
    # vv = (2, 1, 3)
```


### pairwise

隣同士をペアにして返す

```
XY = [(0, 0), (2, 0), (0, 1), (2, 1)]
for (xp, yp), (x, y) in pairwise(XY): # 隣同士をペアにして返す
    print((xp, yp), (x, y))
# [stderr] ??? = (0, 0) ??? = (2, 0)
# [stderr] ??? = (2, 0) ??? = (0, 1)
# [stderr] ??? = (0, 1) ??? = (2, 1)
```


### heapq 優先度付きキューから最小値を取り出す(O(logN))

https://qiita.com/ell/items/fe52a9eb9499b7060ed6

```
#heapq.heapify(リスト)でリストを優先度付きキューに変換。
#heapq.heappop(優先度付きキュー (=リスト) )で優先度付きキューから最小値を取り出す。
#heapq.heappush(優先度付きキュー (=リスト) , 挿入したい要素)で優先度付きキューに要素を挿入。
```

### 動的計画法は再帰で表せ

再帰で表す．そしてメモ化．速くしたければDPテーブル化  
http://blog.unnono.net/2010/05/blog-post_26.html

### 累積和

```
from itertools import accumulate
A = [0, 1, 2, 3]
print(list(accumulate(A))) # [0, 1, 3, 6]
```

### `"! 1 2 3"`,`"? 1 2 3"` など標準出力する方法

```
data = [1,2,3,4,5]
print(" ".join(["!"]+list(map(str,data))),flush=True)
print(" ".join(["?"]+list(map(str,data))),flush=True)
```

### `range`

```
n = 10
for i in range(n):
    print(i)  # 0,1,2,3...9
# 逆順
for i in range(n)[::-1]:
    print(i)  # 9,8,7,6...0
# 逆順(間違い易い)
for i in range(n-1,-1,-1):
    print(i)  # 9,8,7,6...0
```

### 値の交換

```
a,b,c = 1,2,3
print(a,b,c)  # 1,2,3
a,b,c = c,a,b
print(a,b,c)  # 3,1,2
```

### 回分判定

```
# 回分判定
# s:入力文字列
# return: 
#   True:回分である
#   False:回分でない
def is_palindrome(s):
    for ii in range(len(s)//2):
        if s[ii] != s[-ii-1]:
            return False
    return True
```

### set同士は引き算が可能

```
current = {1,2,3,4,5}
target  = {1,3,5,7,9}
print(current - target) # {2,4}
print(target - current) # {7,9}
```

### Yeild

```
def count_up():
    print("開始")
    yield 1        # ここで一時停止、1を返す
    print("再開1")
    yield 2        # ここで一時停止、2を返す
    print("再開2") 
    yield 3        # ここで一時停止、3を返す
    print("終了")

# 実行例
gen = count_up()
print(next(gen))  # "開始" が出力されて 1 が返される
print(next(gen))  # "再開1" が出力されて 2 が返される
print(next(gen))  # "再開2" が出力されて 3 が返される
```

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
[2つの円の位置関係](https://manabitimes.jp/math/745)
