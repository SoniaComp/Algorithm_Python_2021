// 연속이라는 조건이 추가됨
// 연속, 증가, 감소--> 두개씩 비교할 수 있다.
// D[i][j] = i 에서
// i를 1,2,3의 합으로 나타내는 방법의 수
// j를 마지막에 사용한 수

// 초기화해서, 중복이 발생한 경우, 예외처리 해주어야 함.
#include <stdio.h>
long long d[1000001][4];
const long long mod = 1000000009LL;
const int limit = 100000;
int main()
{
  // 초기값 설정
  d[1][1] = 1;
  d[2][2] = 1;
  d[3][3] = 1;
  for (int i = 1; i <= limit; i++)
  {
    if (i - 1 > 0)
    {
      d[i][1] = d[i - 1][2] + d[i - 1][3];
      // 초기값 설정 방법2
    }
    if (i - 2 > 0)
    {
      d[i][2] = d[i - 2][1] + d[i - 2][3];
    }
    if (i - 3 > 0)
    {
      d[i][3] = d[i - 3][1] + d[i - 3][2];
    }
    // 나머지 계산할 떄는 미리 계산
    d[i][1] %= mod;
    d[i][2] %= mod;
    d[i][3] %= mod;
  }
  int t;
  scanf("%d", &t);
  while(t--){
    int n;
    scanf("%d", &n);
    printf("%lld\n", (d[n][1]+d[n][2]+d[n][3])%mod);
  }
}