#include <iostream>
#include <vector>

using namespace std;

int main(){
  vector<int> array; 
  // 사이즈를 반드시 정해주어야 하는 array
  // vector는 사이즈를 그때그때 바꿔줄 수 있음

  vector<int> array2 = {1,2,3,4,5};
  cout << array2.size() << endl;
  array2.resize(10);

  for (auto &itr : array2) cout << itr << "";
  cout << endl;

  vector<int> array3 = {1,2,3,};
  cout << array3.size() << endl;

  // vector의 장점은 new, delete 이런 거 안해도 되고, 메모리가 새지 않고, 자동으로 해줌.
  // 자기의 길이를 알아서 기억해줌.
  
  return 0;
}