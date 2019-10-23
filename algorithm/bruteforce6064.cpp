// 건너뛰며 해보기
// 필요가 없는건 건너뛴다.
// M, N <= 4만 : 16억
// M의 값이 정해져 있을 때, M만 먼저 체크하면 됨.

#include <iostream>
using namespace std;
int main(){
  int t;
  cin >> t;
  while(t--){
    int m, n, x, y;
    cin >> m >> n>> x>> y;
    x -= 1; // 나머지 연산을 위해서
    y -= 1;
    bool ok = false;
    for(int k=x; k<(n*m); k+= m){
      if(k%n == y){
        cout << k+1 <<'\n';
        ok = true;
        break;
      }
    }
    if(!ok){
      cout << -1 <<'\n';
    }
  }
  return 0;
}