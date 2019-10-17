// C++ 에서는 함수뿐만 아니라 연산자도 오버로딩이 가능하다.
#include <iostream>
using namespace std;

class Point
{
private:
  int xpos, ypos;

public:
  Point(int x = 0, int y = 0)
  {
  }
  void showPosition() const
  {
    cout << '[' << xpos << ', ' << ypos << ']' << endl;
  }
  Point operator+(const Point &ref)
  {
    Point pos(xpos + ref.xpos, ypos + ref.ypos);
    return pos;
  }
};

int main(void)
{
  Point pos1(3, 4);
  Point pos2(10, 20);
  // 멤버별 덧셈결과로 새로운 Point 객체가 만들어지고 이것이 반환되어 pos3를 초기화한다.
  // 이 과정에서 복사 생성자가 호출된다.
  Point pos3 = pos1.operator+(pos2);

  // 1. 멤버함수를 호출할 객체
  // 2. 함수의 이름: 기본자료형 변수가 아닌 객체일 경우, operator를 앞에 붙여서, +, - 연산자를 해석한다.
  // 3. 함수의 전달인자
  // 아래 문장은 위 문장과 정확하게 동일하다.
  // Point pos3 = pos1+pos2;

  pos1.showPosition();
  pos2.showPosition();
  pos3.showPosition();
  return 0;
}