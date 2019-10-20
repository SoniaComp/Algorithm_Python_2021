// 하나씩 하나씩 다 해보고
// 답을 구하는 알고리즘
// 비밀번호 찾을 때 0000~9999 다 입력해봄
// 방법의 개수가 많지 않을 때 사용
// 보통 1억 1초
#include <iostream>
#include <algorithm>
using namespace std;
int a[9];
int n=9;
int main() {
  int sum = 0;
  for(int i=0; i<n; i++){
    cin >> a[i];
    sum += a[i]; // 9명 키의 합
  }
  sort(a, a+n);
  // 정렬
  for(int i=0; i<n; i++){
    for(int j=i+1; j<n; j++){ //중복 없애기
      if (sum - a[i] - a[j] == 100){ // 같을 경우
        for(int k=0; k<n; k++){
          if(i==k||j==k) continue;
          cout << a[k] << '\n';
        }
        return 0;
      }
    }
  }
  return 0;
}