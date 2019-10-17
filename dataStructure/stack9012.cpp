// 괄호 문제
#include <iostream>
#include <string>
using namespace std;
string valid(string s)
{
  int cnt = 0;
  for (int i = 0; i < s.size(); i++)
  {
    if (s[i] == '(')
    {
      cnt += 1; // 여는 문자 등장
    }
    else
    {
      cnt -= 1;
    }
    if (cnt < 0)
    {
      return "NO"; // 여는 괄호 부족
    }
  }
  // 모든 과정 끝
  if (cnt == 0)
  {
    return "YES";
  }
  else
  {
    return "NO";
  }
}

int main()
{
  int t;
  cin >> t;
  while (t--)
  {
    string s;
    cin >> s;
    cout << valid(s) << '\n';
  }
  return 0;
}