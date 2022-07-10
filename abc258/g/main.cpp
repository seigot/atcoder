#include<iostream>
#include<algorithm>
#include<bitset>

using namespace std;

int main(){
  int N;
  cin >> N;

  // bitset class
  // https://cpprefjp.github.io/reference/bitset/bitset.html
  vector<bitset<3001>> edge(N);
  // bitを設定する(set:任意の位置のビットを設定する)
  for(int i = 0;i < N;i++){
    for(int j = 0;j < N;j++){
      char c;
      cin >> c;
      if(c == '1')
        // edge_iのjの位置のbitを立てる
	    edge[i].set(j);      
    }
  }
  long long ans = 0;
  for(int i = 0;i < N;i++){
    for(int j = 0;j < N;j++){
      if(!edge[i][j])
        continue;
      // edge_iからみた時のedge_jと隣接しているbitの数を数える(ただし全探索すると6回重複するので最後に6で割る)
      ans += (edge[i] & edge[j]).count();
    }
  }
  cout << ans / 6 << endl;
}

