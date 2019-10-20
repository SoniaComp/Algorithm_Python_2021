#include <iostream>
using namespace std;
int main() {
  int E, S, M;
  cin >> E >> S >> M;
  int e=1, s=1, m=1;

  // 시간 계산을 해보면 얼마 안되니 직접 계산하자
  for(int i=1;;i++){
    // 값이 같은지 확인
    if(e == E && s==S && m==M){
      cout <<i <<'\n';
      break;
    }
    // e, s, m을 동시에 증가시켜가며 체크
    e += 1;
    s += 1;
    m += 1;
    if(e == 16){
      e=1;
    }
    if(s==29){
      s=1;
    }
    if(m==20){
      m=1;
    }
  }
  return 0;
}