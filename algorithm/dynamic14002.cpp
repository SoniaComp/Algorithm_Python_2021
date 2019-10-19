// 실제로 그 수가 무엇인지를 구해야 함.
// 역추적
#include <iostream>
using namespace std;
int a[1000];
int d[1000];
int v[1000];
void go(int p){
  // ? -> ? -> ,,, a[v[p]]-> a[p]
  if (p == -1){
    return;
  }
  // 가장 아래 단계부터 출력된다.
  go(v(p));
  cout << a[p] <<' ';
}

int main(){
  int n;
  cin >> n;
  for(int i=0; i<n; i++){
    cin >> a[i];
  }
  for(int i=0; i<n; i++){
    d[i]= 1;
    v[i]=-1;
    for(int j=0;j<i;j++){
      if(a[j]<a[i]&& d[i]<d[j]+1){
        d[i] = d[j]+1;
        v[i] = j;
      }
    }
  }
  int ans = d[0];
  int p = 0;
  for(int i=0;i<n;i++){
    if(ans<d[i]){
      ans = d[i];
      p = i;
    }
  }
  cout <<ans<<'\n';
  go(p);
  cout<<'\n';
  return 0;
}