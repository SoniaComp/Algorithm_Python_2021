// 단계 하나랑 나머지 전체를 나누는 것
// 점화식 찾기
// D[n] = D[n-1] + D[n-2]
// D[1] = 1
// D[2] = 2
#include <iostream>
using namespace std;
int d[10001];
int main()
{
  int n;
  cin >> n;
  d[1] = 1;
  d[2] = 2;
  for (int i = 3; i < n + 1; i++)
  {
    d[i] = d[i - 1] + d[i - 2] + d[i - 2];
    d[i] %= 10007;
  }
  cout << d[n] << '\n';
  return 0;
}