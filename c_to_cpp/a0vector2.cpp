#include <iostream>
#include <vector>
using namespace std;
// 데이터를 효율적으로 관리
// 배열: index 로 접근
// ------------- 객체 배열: 배열의 요소가 객체가 됨 ------------- //
// 단점: 배열 크기 변경 불가
// 배열 요소가 객체로 구성된 배열로 일반 배열과 같이 사용한다.
class Book
{
private:
  string name;
  int no;

public:
  Book() { cout << " --- Constructor --- " << endl; }
  Book(string s, int n)
  {
    cout << " --- Constructor --- " << endl;
    name = s;
    no = n;
  }

  void setName(string s) { name = s; }
  void setNo(int n) { no = n; }

  string getName() { return name; }
  int getNo() { return no; }
};

// int main()
// {
//   Book books[5];
//   Book books2[5] = {
//       Book("c", 1),
//       Book("C++", 2),
//       Book("Java", 3)};
//   Book books3[] = {
//     Book("c", 1),
//     Book("C++", 2)
//   };
// }

// ------------- 벡터 ------------- //
// 배열 크기 변경 가능
// 정적인 배열의 단점을 보완한 동적 배열로 데이터를 쉽고 효율적으로 관리할 수 있다.
class BankAccount
{
private:
  string a_name;
  int a_no;

public:
  BankAccount() { cout << " --- Constructor --- " << endl; }
  BankAccount(string s, int n)
  {
    cout << " --- Constructor --- " << endl;
    a_name = s;
    a_no = n;
  }

  void setName(string s) { a_name = s; }
  void setNo(int n) { a_no = n; }

  string getName() { return a_name; }
  int getNo() { return a_no; }
};

int main()
{
  vector<BankAccount> bankAccounts(5);
  bankAccounts[0].setName("박찬호");
  bankAccounts[0].setNo(1);
  // 추가 (배열의 크기를 늘림)
  BankAccount ac = BankAccount();
  bankAccounts.push_back(ac);
  // BankAccount 객체를 늘리는데, 그 객체의 이름을 넣어준다.

  // 제거
  bankAccounts.pop_back();

  // 크기
  bankAccounts.size();

  // 반복자
  vector<BankAccount>::iterator iter;
  // 내가 사용하고 있는 벡터의 iterator를 만들어주고 그것의 인스턴스 명을 iter로 지정한다.
  // 처음 주소값 이후 하나씩 하나씩 이동하면서 요소를 가리킨다.

  // 처음 인스턴스 주소값
  iter = bankAccounts.begin();
  // 마지막 인스턴스 주소값 +1
  iter = bankAccounts.end();
  // 제거
  // - 배열의 요소를 삭제.. iter가 가리키고 있는 요소가 제거된다.
  // end() 위치에 있을 경우 한칸 앞으로 와서 맨 마지막 요소를 제거
  bankAccounts.erase(iter);
  return 1;
}