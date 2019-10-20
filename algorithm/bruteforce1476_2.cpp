#include <iostream>
using namespace std;
int main(){
  int e, s, m;
  cin >> e >> s >> m;
  // 1을 빼주는 이유: 15일 경우에는 나누면 0이 되버리는데, 그걸 15로 바꾸어주어야 함.
  // 1을 빼줌으로 0~14로 바꾸어줌 --> 나머지로 만들어주기
  e -= 1;
  s -= 1;
  m -= 1;
  for(int i=0;;i++){
    if(i%15==e&&i%28==s&&i%19==m){
      cout << i+1 << '\n';
      break;
    }
  }
}