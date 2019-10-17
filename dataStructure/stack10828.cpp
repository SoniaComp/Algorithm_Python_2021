#include <iostream>
#include <string>
using namespace std;

// private(class 선언 시 default)
// public(struct 선언 시 default)
struct Stack
{
  int data[10000];
  int size;
  Stack()
  { // 생성자
    size = 0;
  }
  void push(int num)
  {
    data[size] = num;
    size += 1;
  }
  bool empty()
  {
    if (size == 0)
    {
      return true;
    }
    else
      return false;
  }
  int pop()
  {
    if (empty())
    {
      return -1;
    }
    else
    {
      size -= 1;
      return data[size];
    }
  }
  int top()
  {
    if (empty())
    {
      return -1;
    }
    else
    {
      return data[size - 1];
    }
  }
};

int main()
{
  int n;
  cin >> n;

  Stack s;

  while (n--)
  {
    string cmd;
    cin >> cmd;
    if (cmd == "push")
    {
      // cpp는 자료형을 중간에 선언할 수 있다.
      int num;
      cin >> num;
      s.push(num);
    }
    else if (cmd == "top")
    {
      cout << (s.empty() ? -1 : s.top()) << '\n';
    }
    else if (cmd == "size")
    {
      cout << s.size << '\n';
    }
    else if (cmd == "pop")
    {
      cout << (s.empty() ? -1 : s.top()) << '\n';
      if (!s.empty())
      {
        s.pop();
      }
    }
  }
  return 0;
}