// 인접한 자리의 차이가 1이 나는 수를 계단 수라고 한다.
// D[N][L] = 길이가 N인 계단수, 마지막 수 [L]
// D[N][L] = D[N-1][L-1] + D[N-1][L+1]
// 그러나 이게 항상 가능한 것은 아니다. 0인 경우, 9인 경우는 예외 처리
#include <iostream>
#include <vector>
using namespace std;
long long d[101][10];
long long mod = 1000000000;
int main(){
  int n;
  cin >> n;
  // 초기값 설정
  for(int i=1;i<=9; i++){
    d[1][i] = 1;
    // 0으로는 시작할 수 없으므로 d[1][0] = 0;
  }
  // 배열의 크기가 늘어날때를 보자
  for (int i=2; i<=n; i++){
    for (int j=0; j<=9; j++){
      d[i][j]=0;
      // 예외처리
      if(j-1>=0){
        d[i][j] += d[i-1][j-1];
      }
      if(j+1<=9){
        d[i][j] += d[i-1][j+1];
      }
      d[i][j] %= mod;
    }
  }
  // 결과값 구하는 중...
  long long ans = 0;
  for(int i=0; i<=9; i++){
    ans += d[n][i];
  }
  ans %= mod;
  cout <<ans <<'\n';
  return 0;
}