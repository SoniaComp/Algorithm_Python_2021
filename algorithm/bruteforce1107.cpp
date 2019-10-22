// +나 -를 누르다가 숫자버튼을 누르면, 그동안 입력한 것이 의미없어진다.
// 의미 없는 것이 있는 방법은 최소가 될 수 없다.

// C에 포함되어 있는 숫자 확인하기
// 1) 수를 문자열로 바꾼 다음, 한 글자씩 검사하는 방법
// 2) 수를 10으로 계속해서 나누면서 하나씨 검사하는 방법
// 버튼이 고장나 있으면 ture, 아니면 false
// 예외처리할게 많다.

#include <iostream>
using namespace std;
bool broken[10]; // 고장난게 있는지 확인
int possible(int c){
  if(c==0){ // 예외처리
    return broken[0] ? 0 : 1;
    // 0이 불가능하면, 아예 불가능
  }
  // possible을 불가능하면 0, 가능하면 버튼을 눌러야 하는 횟수를 리턴하게 변경
  // 고장난 번호가 얼마나 있는지 check
  int len = 0;
  while (c>0){
    if(broken[c%10]){
      return 0;
    }
    len+=1;
    c/=10;
  }
  return len;
}

int main(){
  int n;
  cin >> n;
  int m;
  cin >> m;
  // 고장난거 check
  for(int i=0; i<m; i++){
    int x;
    cin >> x;
    broken[x] = true;
  }
  // 숫자버튼 누르지 않고, +, -만 누를 때의 개수
  // 항상 있는 경우: 초기값
  int ans = n - 100;
  if (ans < 0){
    ans = -ans;
  }
  for (int i=0; i<=1000000; i++){ // i: 숫자버튼을 이용해 이동할 수 있는 버튼의 갯수
  // 50만의 두 배는 그렇게 큰 수가 아니다.
    int c=i; // 눌러줘야할 채널 c를 결정하고,
    int len=possible(c); // 몇번 정할 수 있는지 정해주고,
    if(len>0){ // 0이 아니면, 
      int press = c-n; // +나 -를 몇번 정해야 하는지 확인
      if(press<0){
        press = -press;
      }
      if(ans > len+press){ // 작으면 넣기
        ans = len + press;
      }
    }
  }
  printf("%d\n", ans);
  return 0;
}