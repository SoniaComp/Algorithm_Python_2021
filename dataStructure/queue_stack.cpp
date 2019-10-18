// 큐 이용해서 스택 구현하기
#include <cstdio>
#include <cstring>
#include <queue>

using namespace std;
char a[60000];
int main()
{
  scanf("%s", a);
  queue<char> first, second;
  int n = strlen(a);
  for (int i = 0; i < n; i++)
  {
    first.push(a[i]);
  }
  for (int i = 0; i < n; i++)
  {
    second.push(first.front());
    first.pop();
  }
  for (int i = 0; i < n; i++)
  {
    second.front();
    second.pop();
  }
}