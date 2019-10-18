// n을 1,2,3의 합으로 나타내는 방법의 수
// D[n] = D[n-1] + D[n-2] + D[n-3]
#include <iostream>
int d[12];
using namespace std;
// 문자열도 크기가 0인경우도 하나로 셈
// 그래서 0인 경우에는 아무것도 사용하지 않는 방법이 하나
int main()
{
  d[0] = 1;
  d[1] = 1;
  d[2] = 2;
  d[3] = 4;
  for (int i = 4; i <= 11; i++)
  {
    d[i] = d[i - 1] + d[i - 2] + d[i - 3];
  }
  /*
  // 이렇게도 짤 수 있다!
  for (int i=1; i<=10; i++) {
        if (i-1 >= 0) {
            d[i] += d[i-1];
        }
        if (i-2 >= 0) {
            d[i] += d[i-2];
        }
        if (i-3 >= 0) {
            d[i] += d[i-3];
        }
    }
  */
  int t;
  scanf("%d", &t);
  while (t--)
  {
    int n;
    scanf("%d", &n);
    printf("%d\n", d[n]);
  }
}