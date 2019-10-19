// 카드팩 최대한 저렴하게 사기
// D[n]: 카드 n개를 구매하는 비용의 최대값
// D[n] = D[n-i] + P[i]
// D[n] = max(D[n-i]+p[i])
// 변수가 들어가 있는 경우, 변수의 범위를 정해줘야 한다.
// 1<= i<=n

// 배열의 초기값을 잘 설정해주어야 한다.
// 초기값 설정 방법 1
// d[i] = 1000*10000최대값
// 초기값 설정 방법 2 - 추천
// 경우의 수 0도 의미를 갖음
// for (int i=1; i<=n; i++){
//  d[i] = -1;
// }
// -1은 아직 정답을 구하지 않았다는 의미
// if(d[i]==-1) 대입
#include <iostream>
#include <vector>
using namespace std;
int main()
{
  int n;
  cin >> n;
  vector<int> a(n + 1);
  for (int i = 1; i <= n; i++)
  {
    cin >> a[i];
  }
  vector<int> d(n + 1, -1); //-1로 초기화. 아직 값이 설정되지 않았음
  d[0] = 0;
  for (int i = 1; i <= n; i++)
  {
    for (int j = 1; j <= i; j++)
    {
      if (d[i] == -1 || d[i] > d[i - j] + a[j])
      {
        d[i] = d[i - j] + a[j];
      }
    }
  }
  cout << d[n] << '\n';
  return 0;
}