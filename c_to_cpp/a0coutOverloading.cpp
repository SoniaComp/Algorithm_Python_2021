#include <iostream>

namespace mystd
{
using namespace std;

class ostream
{
public:
  // ostream& operator<< (char *str)
  void operator<<(char *str)
  {
    printf("%s", str);
  }
  void operator<<(char str)
  {
    printf("%c", str);
  }
  void operator<<(ostream &(*fp)(ostream &ostm))
  {
    fp(*this);
  }
};
ostream &endl(ostream &ostm)
{
  ostm << '\n';
  fflush(stdout);
  return ostm;
}
ostream cout;
} // namespace mystd

// <<, >> 연산자의 오버로딩
// ostream &operator<<(ostream &os, const Point &pos)
// {
//   os << '[' << pos.xpos << ', ' << pos.ypos << ']' << endl;
//   return os;
// }