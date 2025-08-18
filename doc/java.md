
## python Tips

[過去問](https://github.com/seigot/atcoder/blob/main/doc/pastexam.md)

### header

```
import java.util.*;
import java.io.*;
import java.math.*;

public class Main {
    static FastScanner sc = new FastScanner();
    static PrintWriter out = new PrintWriter(System.out);
    
    public static void main(String[] args) {
        solve();
        out.flush();
    }
    
    static void solve() {
        // 入力パターンの例
        
        // (1) 数字が1つ
        // Python: N = int(input())
        int N = sc.nextInt();
        
        // (2) 数字が2つ以上で別々に受け取り
        // Python: A, B = map(int, input().split())
        int A = sc.nextInt();
        int B = sc.nextInt();
        
        // 3つ以上の場合
        // Python: A, B, C = map(int, input().split())
        // int A = sc.nextInt();
        // int B = sc.nextInt(); 
        // int C = sc.nextInt();
        
        // (3) 文字列が1つ
        // Python: S = input()
        String S = sc.next();        // スペースで区切られた単語
        // String S = sc.nextLine();   // 行全体（スペースも含む）
        
        // (4) 文字列が2つ以上で別々に受け取り
        // Python: S, T = map(str, input().split())
        String S1 = sc.next();
        String T = sc.next();
        
        // (5) リストで受け取り
        // Python: AB = list(map(int, input().split()))
        int[] AB = sc.nextIntArray(N);
        
        // 別の書き方（要素数が分かっている場合）
        // int[] AB = new int[N];
        // for (int i = 0; i < N; i++) {
        //     AB[i] = sc.nextInt();
        // }
        
        // (6) dequeで受け取り（JavaではArrayDequeを使用）
        // Python: A = deque(map(int, input().split()))
        ArrayDeque<Integer> A = new ArrayDeque<>();
        for (int i = 0; i < N; i++) {
            A.add(sc.nextInt());
        }
        
        // または一行で
        // ArrayDeque<Integer> A = new ArrayDeque<>(Arrays.asList(
        //     Arrays.stream(sc.nextIntArray(N)).boxed().toArray(Integer[]::new)
        // ));
        
        // (7) BigDecimal使用（decimal相当、小数の誤差を正確に扱う）
        // Python: AB = [list(map(Decimal, input().split())) for _ in range(N)]
        BigDecimal[][] ABDecimal = new BigDecimal[N][];
        for (int h = 0; h < N; h++) {
            String[] line = sc.nextLine().split(" ");
            ABDecimal[h] = new BigDecimal[line.length];
            for (int i = 0; i < line.length; i++) {
                ABDecimal[h][i] = new BigDecimal(line[i]);
            }
        }
        
        // (8) maze（スペースなしの2次元配列）
        // Python: maze = [list(input()) for h in range(H)]
        int H = sc.nextInt();
        int W = sc.nextInt();
        char[][] maze = new char[H][];
        for (int h = 0; h < H; h++) {
            maze[h] = sc.next().toCharArray();
        }
        
        // (9) スペースありの2次元配列
        // Python: P = [list(map(int, input().split())) for h in range(H)]
        int[][] P = new int[H][];
        for (int h = 0; h < H; h++) {
            P[h] = sc.nextIntArray(W);  // 列数がWの場合
        }
        
        // 列数が不定の場合
        // int[][] P = new int[H][];
        // for (int h = 0; h < H; h++) {
        //     String[] line = sc.nextLine().split(" ");
        //     P[h] = new int[line.length];
        //     for (int i = 0; i < line.length; i++) {
        //         P[h][i] = Integer.parseInt(line[i]);
        //     }
        // }
    }
    
    // ===== 便利な入力メソッド =====
    
    // 1次元配列の入力（long版）
    static long[] nextLongArray(int n) {
        long[] arr = new long[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextLong();
        }
        return arr;
    }
    
    // 2次元配列の入力（int版）
    static int[][] next2DIntArray(int h, int w) {
        int[][] arr = new int[h][w];
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                arr[i][j] = sc.nextInt();
            }
        }
        return arr;
    }
    
    // 2次元配列の入力（long版）
    static long[][] next2DLongArray(int h, int w) {
        long[][] arr = new long[h][w];
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                arr[i][j] = sc.nextLong();
            }
        }
        return arr;
    }
    
    // 文字列の2次元配列（maze）
    static char[][] nextCharArray(int h) {
        char[][] arr = new char[h][];
        for (int i = 0; i < h; i++) {
            arr[i] = sc.next().toCharArray();
        }
        return arr;
    }
    
    // リスト形式で受け取り
    static List<Integer> nextIntList(int n) {
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            list.add(sc.nextInt());
        }
        return list;
    }
    
    // ペアのリスト
    static List<Pair<Integer, Integer>> nextPairList(int n) {
        List<Pair<Integer, Integer>> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            list.add(new Pair<>(a, b));
        }
        return list;
    }
    
    // グラフの隣接リスト
    static List<Integer>[] nextGraph(int n, int m) {
        @SuppressWarnings("unchecked")
        List<Integer>[] graph = new List[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt() - 1;  // 0-indexedにする場合
            int v = sc.nextInt() - 1;
            graph[u].add(v);
            graph[v].add(u);  // 無向グラフの場合
        }
        return graph;
    }
    
    // 重み付きグラフの隣接リスト
    static List<Edge>[] nextWeightedGraph(int n, int m) {
        @SuppressWarnings("unchecked")
        List<Edge>[] graph = new List[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt() - 1;
            int v = sc.nextInt() - 1;
            int w = sc.nextInt();
            graph[u].add(new Edge(v, w));
            graph[v].add(new Edge(u, w));  // 無向グラフの場合
        }
        return graph;
    }
}

// ===== 補助クラス =====

// Pairクラス
class Pair<T, U> {
    public T first;
    public U second;
    
    public Pair(T first, U second) {
        this.first = first;
        this.second = second;
    }
    
    @Override
    public String toString() {
        return "(" + first + ", " + second + ")";
    }
}

// Edgeクラス
class Edge {
    int to, cost;
    
    Edge(int to, int cost) {
        this.to = to;
        this.cost = cost;
    }
}

// 高速入力クラス
class FastScanner {
    private BufferedReader br;
    private StringTokenizer st;
    
    public FastScanner() {
        br = new BufferedReader(new InputStreamReader(System.in));
    }
    
    public String next() {
        while (st == null || !st.hasMoreElements()) {
            try {
                st = new StringTokenizer(br.readLine());
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return st.nextToken();
    }
    
    public int nextInt() {
        return Integer.parseInt(next());
    }
    
    public long nextLong() {
        return Long.parseLong(next());
    }
    
    public double nextDouble() {
        return Double.parseDouble(next());
    }
    
    public String nextLine() {
        String str = "";
        try {
            str = br.readLine();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return str;
    }
    
    // 配列入力
    public int[] nextIntArray(int n) {
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = nextInt();
        }
        return arr;
    }
    
    public long[] nextLongArray(int n) {
        long[] arr = new long[n];
        for (int i = 0; i < n; i++) {
            arr[i] = nextLong();
        }
        return arr;
    }
    
    public double[] nextDoubleArray(int n) {
        double[] arr = new double[n];
        for (int i = 0; i < n; i++) {
            arr[i] = nextDouble();
        }
        return arr;
    }
}

// ===== 使用例 =====
class InputExamples {
    static void example1() {
        // 例：AtCoder典型的な入力
        // N
        // A1 A2 ... AN
        // H W
        // maze (H行)
        
        int N = sc.nextInt();
        int[] A = sc.nextIntArray(N);
        
        int H = sc.nextInt();
        int W = sc.nextInt();
        char[][] maze = nextCharArray(H);
        
        // 処理...
    }
    
    static void example2() {
        // 例：グラフ問題
        // N M
        // u1 v1
        // u2 v2
        // ...
        // uM vM
        
        int N = sc.nextInt();
        int M = sc.nextInt();
        
        List<Integer>[] graph = nextGraph(N, M);
        
        // 処理...
    }
    
    static void example3() {
        // 例：座標問題
        // N
        // x1 y1
        // x2 y2
        // ...
        // xN yN
        
        int N = sc.nextInt();
        List<Pair<Integer, Integer>> points = nextPairList(N);
        
        // 処理...
    }
}
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

