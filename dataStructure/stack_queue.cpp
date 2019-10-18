// 스택을 이용해 큐 구현하기
#include <cstdio>
#include <cstring>
#include <stack>
using namespace std;
char a[60000];
int main()
{
  scanf("%s", a);
  stack<char> first, second;
  int n = strlen(a);
  for (int i = 0; i < n; i++)
  {
    first.push(a[i]);
  }
  for (int i = 0; i < n; i++)
  {
    second.push(first.top());
    first.pop();
  }
  for (int i = 0; i < n; i++)
  {
    second.top();
    second.pop();
  }
}
