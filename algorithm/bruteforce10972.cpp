// 순열이 매우 중요할 때
// 임의의 수열을 다른 순서로 섞는 연산
// 순열: 모든 순서를 다 시도해봐야 할 때

// 다음 순열
// 사전 순으로 다음에 오는 순열과 이 전에 오는 순열을 찾는 방법

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main(){
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i=0;i<n; i++){
    cin >> a[i];
  }
  if(next_permutation(a.begin(), a.end())){
    for(int i=0;i<n; i++){
      cout << a[i] << ' ';
    }else {
      cout << "-1";
    }
    cout << '\n';
    return 0;
  }
}