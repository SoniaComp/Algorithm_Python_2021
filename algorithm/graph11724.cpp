// 연결 요소
// 이렇게 나누어진 그래프를 연결 요소라고 한다.
// 연결 요소에 속한 모든 정점을 연결하는 경로가 있어야 한다.
// 다른 연결 요소에 속한 정점과 연결하는 경로가 있으면 안된다.

// 연결 그래프: 연결 요소가 몇개인지 알아보려면, DFS, BFS를 이용해주면 됨.
// 두 알고리즘의 목표: 하나의 시작점에서 모든 정점을 다 방문하는 알고리즘
#include <cstdio>
#include <vector>
using namespace std;
vector<int> a[1001];
void dfs(int node){
  check[node] = true;
  for(int i=0; i<a[node].size(); i++){
    int next = a[node][i];
    // 끝나는지 안끝나는지 확인
    if(check[next]==false) dfs(next);
  }
}

int main() {
  int n, m;
  scanf("%d %d", &n, &m);
  // 그래프 만들기
  for(int i=0; i<m; i++){
    int u, v;
    scanf("%d %d", &u, &v);
    a[u].push_back(v);
    a[v].push_back(u);
  }
  int components = 0;
  for (int i=1; i<=n; i++){
    if(check[i]==false){
      dfs(i);
      components += 1;
    }
  }
  printf("%d\n",components);
  return 0;
}