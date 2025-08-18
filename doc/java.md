
## python Tips

[過去問](https://github.com/seigot/atcoder/blob/main/doc/pastexam.md)

### header

```
-
```

### 標準入力

[初心者向けAtcoder標準入力セット(Python)](https://qiita.com/jamjamjam/items/e066b8c7bc85487c0785)

```
-                     # (1)数字が1つ 入力例:N
```

```
-      # (2)数字が2つ以上で別々に受け取り  入力例:A B
```

```
-                          # (3)文字列が1つ 入力例:S 
```

```
-      # (4)文字列が2つ以上で別々に受け取り 入力例:S T
```

```
-  # (5)リストで受け取り 入力例:A1 A2 ... An
```

```
-  # (6)dequeueで受け取り 入力例:A1 A2 ... An
```

```
- # decimal(小数の誤差を正確に扱う)使う場合はpython3にする(pypyだと遅い)
```

```
- # maze(###.###) のようなスペースなしの2次元配列で受け取り
- # 1 2 3 4 のようなスペースありの2次元配列を受け取り
```

### 変数の宣言

```
# graph (N頂点M辺)
-
```

```
# 2次元配列 ( (10**5)*(10**5)のようなサイズは宣言時にエラーになるので注意 )
-
## defaultdictを使う場合
-
# 3次元配列
-
```

### テスト用の入力

```
-
```

### よく使う機能

| 概要 |  処理  |  説明  |  備考  |
| ---- | ---- | ---- | ---- |
|  list操作  |  list  |  -  |  list = [] で初期化、(1次元配列の場合は`list = [0]*10`で初期化)  |
|  辞書操作 | dict | - | `dict1 = {'X': 2, 'Y': 3, 'Z': 4}`で初期化 |
|  文字列操作  |  String  |  -  |  S="xxx" で初期化  |
|  集合  |  set  |  注意：pythonのsetの表示される順番は保証されない   |  初期化:`s = set()` |
|  計数  |  Counter  |  listの要素をカウント(辞書型)  |  `from collections import Counter`、`c = Counter(l)` |
|  キュー  |  dequeue  |  -  |  `d = deque(['a', 'b', 'c'])`で初期化,[配列アクセスの計算量はO(N)](https://qiita.com/snhrhdt/items/2e514d4d6af983fcf6f0)  |
|  変換  |  chr()  |  ascii-->charに変換  |  `chr(ord("A")+1)-->B`  |
|  演算子  |  **  |  べき乗  |  10の18乗(=`inf = 10**18`), powの方が高速  |
|  定数  |  math.pi  |  π  |  角度(°)から弧度(rad)への変換式:`rad=theta*math.pi/180`  |
|  関数(補間)  |  comb()  |  コンビネーション  |  [comb.py](https://github.com/seigot/tools/blob/master/atcoder/comb.py)  |
|  その他  |  exit(0)  |  正常終了  |  -  |

### zip/enumerate

```
-
```

### sort

```
-
```

### 集合

#### 部分集合/超集合を判定`issubset/issuperset`)

```
-
```

#### 空集合かどうかを判定

```
-
```

### 二次元配列探索時のindex

4方向

```
-
```

8方向

```
-
```

### combinations

```
-
```

### combinations_with_replacement

組合せ(重複あり)

```
-
```

### permutations

```
-
```

### permutations(next_permutationsの代わり)

```
-
```

### product

```
-
```


### pairwise

```
-
```

### heapq 優先度付きキューから最小値を取り出す(O(logN))

```
-
```

### 累積和

```
-
```

### `"! 1 2 3"`,`"? 1 2 3"` など標準出力する方法

```
-
```

### `range`

```
-
```

### 値の交換

```
-
```

### 回分判定

```
-
```

### set同士は引き算が可能

```
-
```

### Yeild

```
-
```

### 参考

-

