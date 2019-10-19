// 카드팩 최대한 비싸게 사기
// D[n]: 카드 n개를 구매하는 비용의 최대값
// D[n] = D[n-i] + P[i]
// D[n] = max(D[n-i]+p[i])
// 변수가 들어가 있는 경우, 변수의 범위를 정해줘야 한다.
// 1<= i<=n
#include <iostream>
#include <vector>
using namespace std;
int main()
{
  int n;
  cin >> n;
  vector<int> a(n + 1);
  // 카드팩의 개수 N개
  for (int i = 1; i <= n; i++)
  {
    cin >> a[i];
  }
  vector<int> d(n + 1);
  // n개 구매하기 위한 최대비용
  // 초기값 0
  for (int i = 1; i <= n; i++)
  {
    for (int j = 1; j <= i; j++)
    {
      d[i] = max(d[i], d[i - j] + a[j]);
      // 쪼개는게 더 큰지, 그냥이 더 큰지 확인
    }
  }
  cout << d[n] << '\n';
  return 0;
}