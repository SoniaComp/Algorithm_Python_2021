#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>
using namespace std;
vector<int> a[1001];
void dfs(int node){
  check[node] = true;
  printf("%d ", node);
  // 공간잡도 O(V^2)
  for(int i=0; i<a[node].size();i++){
    int next = a[node][i]; // 체크하기
    if (check[next]==false){
      dfs(next); // 재귀로 구현
    }
  }
}
void bfs(int start){
  queue<int> q;
  memset(check, false, sizeof(check));
  check[start] = true;
  q.push(start);
  while(!q.empty()){
    int node = q.front();
    q.pop();
    printf("%d ", node);
    for(int i=0; i<a[node].size(); i++){
      int next = a[node][i];
      if (check[next]==false){
        check[next] = true;
        q.push(next);
      }
    }
  }
}

int main(){
  // 정점의 개수, 간선의 개수, 탐색 시작할 정점의 번호
  int n, m, start;
  scanf("%d %d %d", &n, &m, &start);
  // 간선 모두 표기
  for(int i=0; i<m; i++){
    int u, v;
    scanf("%d %d", &u, &v);
    // 양방향 그래프
    // 인접리스트
    a[u].push_back(v);
    a[v].push_back(u);
  }
  // sort
  // sort(start, end)를 이용하여, (start, end)의 범위에 있는 인자(element)를 오름차순(default)으로 정리해주는 함수
  // start를 포함하고 end를 포함하지 않는 구간
  // 퀵정렬 기반
  // 시간 복잡도 nlogn
  // 작은 수부터 정렬
  for(int i=1; i<=n; i++){
    sort(a[i].begin(), a[i].end());
  }
  dfs(start);
  puts("");
  bfs(start);
  puts("");
  return 0;
}