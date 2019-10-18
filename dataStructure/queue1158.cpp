// 순환큐
#include <cstdio>
#include <queue>
using namespace std;
int main()
{
  int n, m;
  scanf("%d %d", &n, &m);
  queue<int> q;
  for (int i = 1; i <= n; i++)
  {
    q.push(i);
  }
  printf("<");
  for (int i = 0; i < n - 1; i++)
  {
    for (int j = 0; i < m - 1; j++)
    {
      q.push(q.front()); // 앞에꺼를 뒤로 밀어넣기
      q.pop();
    }
    printf("%d, ", q.front());
    q.pop();
  }
  printf("%d\n", q.front()); // 마지막 꺼 빼기
  return 0;
}