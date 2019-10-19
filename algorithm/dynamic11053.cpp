// Longest Increasing subsequence [LIS]
// 부분수열: 순서를 유지하며 띄엄띄엄 읽는 것
// 직접 해보면서 확인해보기(귀납적 사고)
// A[i]를 마지막으로 하는 가장 긴 증가하는 부분수열의 길이
// D[i] = max(D[j]) + 1
// j < i, A[j] < A[i]
// 시간 복잡도 O(n^2)
// 전체 D[i]중 최대값

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main(){
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i=0; i<n; i++){
    cin >> a[i];
  }
  vector<int> d(n);
  for(int i=0; i<n; i++){
    d[i] = 1; // 우선 초기값
    // 앞에 보면서 바꾸어주기
    for (int j=0; j<i; j++){
      // 앞에 있는 숫자보다 작고, d[j]가 커진다면,
      if(a[j]<a[i] && d[j]+1>d[i]) d[i] = d[j]+1;
    }
  }
  // max 찾기
  cout << *max_element(d.begin(), d.end())<<'\n';
  return 0;
}