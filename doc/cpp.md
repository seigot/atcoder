## C++ Tips

## compile

compile

```
g++ -std=gnu++17 -Wall -Wextra -O2 -DONLINE_JUDGE main.cpp
```

実行

```
./a.out
```

[atcoder rules C++ (GCC 9.2.1)](https://atcoder.jp/contests/APG4b/rules?lang=ja)

## header

```
xxx
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
#### (5)リストで受け取り 入力例:A1 A2 ... An  
#### (6)dequeueで受け取り 入力例:A1 A2 ... An  
#### maze(###.###)を2次元配列で受け取り  

## 出力
- 文字列または数字 A を改行つきで表示
- ベクトル vec を1要素ごとに改行して出力
- リスト vec を空白区切りで出力

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
for (int i = 0; i < vec.size()-1; i ++){
  cout << vec.at(i) << " ";
}
cout << vec.back() << endl;
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
