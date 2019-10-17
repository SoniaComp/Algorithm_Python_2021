#include <iostream>
#include <array>
#include <algorithm>

using namespace std;

void printLength(const array<int, 5> &my_arr)
{
  cout << my_arr.size() << endl;
}

int main()
{
  // int arr[5] = {1,2,3,4,5};
  array<int, 5> my_arr = {1, 2, 3, 4, 5};
  // my_arr = { 0, 1, 2, 4}; // 나머지는 0으로 채워줌

  // cout << my_arr[10] << endl;    // 무조건 access
  // cout << my_arr.at(10) << endl; // index가 있는지 확인해보고 없다면 예외처리. 약간 느림
  cout << my_arr.size() << endl;

  for (auto element: my_arr) cout << element << " " ;
  cout << endl;

  std::sort(my_arr.rbegin(), my_arr.rend()); // r을 넣으면 역순으로 정렬

  return 0;
}