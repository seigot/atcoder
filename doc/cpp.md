## C++ Tips

[C++入門 AtCoder Programming Guide for beginners (APG4b)](https://atcoder.jp/contests/APG4b)

## compile

compile

```
g++ -std=gnu++17 -Wall -Wextra -O2 -DONLINE_JUDGE main.cpp
```

```
# 省略版
g++ main.cpp
```

実行

```
./a.out
```

[atcoder rules C++ (GCC 9.2.1)](https://atcoder.jp/contests/APG4b/rules?lang=ja)

## header

```
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cassert>
#include<cmath>
#include<vector>
#include<map>
#include<set>
#include<string>
#include<queue>
#include<stack>
using namespace std;
#define MOD 1000000007
#define MOD2 998244353
#define INF ((1<<30)-1)
#define LINF (1LL<<60)
#define EPS (1e-10)
typedef long long Int;
typedef pair<Int, Int> P;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
int main(){
    cin >> n;
    int ans = 0;
    cout << ans << endl;
    return 0
}
```

## 標準入力

- (1)数字が1つ 入力例:N  
- (2)数字が2つ以上で別々に受け取り  入力例:A B  
- (3)文字列が1つ 入力例:S   
- (4)文字列が2つ以上で別々に受け取り 入力例:S T  
- (5)リストで受け取り 入力例:A1 A2 ... An  
- (6)dequeueで受け取り 入力例:A1 A2 ... An  
- maze(###.###)を2次元配列で受け取り  

#### (1)数字が1つ 入力例:N 
```
int N
cin >> N;
```
入力が小数、文字列の場合は, int の部分をそれぞれ double, string にすればよい
#### (2)数字が2つ以上で別々に受け取り  入力例:A B  
```
int N, M;  
cin >> N >> M ;
```
入力が小数、文字列の場合は, int の部分をそれぞれ double, string にすればよい
#### (3)文字列が1つ 入力例:S   
```
vector<int> vec(N);
for (int i = 0; i < N; i++) {
  cin >> vec.at(i);
}
```
  
#### (4)文字列が2つ以上で別々に受け取り 入力例:S T  
```
string S, T;  
cin >> S >> T;
```

#### (5)リストで受け取り 入力例:A1 A2 ... An  

```
int A[N];
for (int i = 0; i < N; i++) {
  cin >> A[i];
}
```

#### (6)dequeueで受け取り 入力例:A1 A2 ... An  

#### maze(###.###)を2次元配列で受け取り  
```
string field[W];
for(int j = 0;j < H;j++) cin >> field[j];
```

## 出力
- 文字列または数字 A を改行つきで表示
- ベクトル vec を1要素ごとに改行して出力
- リスト vec を空白区切りで出力
- 小数値を出力

#### 文字列または数字 A を改行つきで表示

```
cout << A << endl;
```

#### ベクトル vec を1要素ごとに改行して出力

```
for(auto v: vec){
  cout << v << endl;
}
```

#### リスト vec を空白区切りで出力

```
#include <vector>
std::vector<int> vec;
vec.push_back(1);

for (int i = 0; i < vec.size()-1; i ++){
  cout << vec.at(i) << " ";
}
cout << vec.back() << endl;
```

#### 小数値を出力

```
int val = 0.001
printf("%.10lf\n", val);
```


### テスト用の入力

```
g++ -std=gnu++17 -Wall -Wextra -O2 -DONLINE_JUDGE main.cpp
./a.out
## 標準入力から値を入力
```


## 便利なライブラリ

[bitset](https://cpprefjp.github.io/reference/bitset/bitset.html)


## 参考

[プログラミングコンテストにおける C++ での標準入出力のまとめ](https://wakabame.hatenablog.com/entry/2019/02/24/141009)
[std::sort](https://kaworu.jpn.org/cpp/std::sort#.E9.99.8D.E9.A0.86.E3.81.A7.E3.82.BD.E3.83.BC.E3.83.88.E3.81.99.E3.82.8B.E4.BE.8B)

