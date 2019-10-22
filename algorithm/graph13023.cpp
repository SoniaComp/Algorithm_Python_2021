// 친구관계: 간선
// 사람: 정점

// 간선리스트 모두 순회하며, 간선이 있는지 Check

// 간선리스트 -> 모든 간선을 찾는 것
// 인접 리스트 -> 임의의 정점과 연결된 간선을 찾는 것

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
bool a[2000][2000];
vector<int> g[2000];
vector<pair<int,int>> edges;
int main() {
    int n, m;
    cin >> n >> m;
    for (int i=0; i<m; i++) {
        int from, to;
        cin >> from >> to;
        edges.push_back({from, to});
        edges.push_back({to, from});
        a[from][to] = a[to][from] = true;
        g[from].push_back(to);
        g[to].push_back(from);
    }
    m *= 2;
    for (int i=0; i<m; i++) {
        for (int j=0; j<m; j++) {
            // A -> B
            int A = edges[i].first;
            int B = edges[i].second;
            // C -> D
            int C = edges[j].first;
            int D = edges[j].second;
            if (A == B || A == C || A == D || B == C || B == D || C == D) {
                continue;
            }
            // B -> C
            if (!a[B][C]) {
                continue;
            }
            // D -> E
            for (int E : g[D]) {
                if (A == E || B == E || C == E || D == E) {
                    continue;
                }
                cout << 1 << '\n';
                return 0;
            }
        }
    }
    cout << 0 << '\n';
    return 0;
}