// 연결된거를 하려면, 간선을 이룬다.
// 연결 요소의 개수를 구하고, 연결 요소의크기를 구하는 알고리즘
// BFS, DFS
// 인접리스트를 사용할 필요 없다.
// d[i][j] = (i, j) 방문안했으면 0, 방문했으면 단지 번호

// 정점 번호가 x 하나였는데, x행, y열
int cnt = 0;
for(int i=0;i<n;i++){
  for(int j=0;j<n;j++){
    if(a[i][j]==1&&d[i][j]==0){
      bfs(i, j, ++cnt);
    }
  }
}
// cnt : 단지 번호

void bfs(int x, int y, int cnt){
  queue<pair<int, int>> q;
  q.push(make_pair(x, y));
  d[x][y] = cnt;
  while(!q.empty()){
    x = q.front().first;
    y = q.front().second;
    q.pop();
    for(int k=0; k<4; k++){
      int nx = x+dx[k], ny= y+dy[k];
      if(0<=nx&&nx<n&&0<=ny&&ny<n){
        if(a[nx][ny]==1&&d[nx][ny]==0){
          q.push(make_pair(nx, ny);
          d[nx][ny]=cnt;)
        }
      }
    }
  }
}