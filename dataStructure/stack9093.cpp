//단어 최대 20, 문장의 길이 최대 1000 단아 단어 사이에 공백이 하나
#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int t;
  cin >> t;
  cin.ignore(); // 입력받고
  while (t--)
  {
    string str;
    getline(cin, str); // 다시 불러옴 getline
    str += '\n';
    stack<char> s; // stack을 만든다.
    for (char ch : str)
    {                              // stack을 돌면서
      if (ch == ' ' || ch == '\n') // 공백이나 줄바꿈을 만난다면
      {
        while (!s.empty())
        {
          cout << s.top();
          s.pop();
        }
      }
      else
      {
        s.push(ch); // 그 전에는 넣는다.
      }
    }
  }
  return 0;
}