// 테트로미노를 하나를 적절히 놓아서, 쓰여있는 수들의 합을 최대로 하는 프로그램
// 회전이나 대칭을 시켜도 된다.
// 문제의 단계
// 1. 어떤 테트로미노를 놓을 건지 - 19가지(회전여부에 따른 변화를 다른 걸로 볼때)
// 2. 어디에 놓을 건지(N*M가지)

// 1. 19가지 블록을 전부 사용
// 2. 위치 값 저장

// 경우의 수 구하기#include <iostream>
using namespace std;
int a[500][500];
int main() {
    int n, m;
    cin >> n >> m;
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            cin >> a[i][j];
        }
    }
    int ans = 0;
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            if (j+3 < m) {
                int temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i][j+3];
                if (ans < temp) ans = temp;
            }
            if (i+3 < n) {
                int temp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+3][j];
                if (ans < temp) ans = temp;
            }
            if (i+1 < n && j+2 < m) {
                int temp = a[i][j] + a[i+1][j] + a[i+1][j+1] + a[i+1][j+2];
                if (ans < temp) ans = temp;
            }
            if (i+2 < n && j+1 < m) {
                int temp = a[i][j] + a[i][j+1] + a[i+1][j] + a[i+2][j];
                if (ans < temp) ans = temp;
            }
            if (i+1 < n && j+2 < m) {
                int temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+2];
                if (ans < temp) ans = temp;
            }
            if (i+2 < n && j-1 >= 0) {
                int temp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+2][j-1];
                if (ans < temp) ans = temp;
            }
            if (i-1 >= 0 && j+2 < m) {
                int temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i-1][j+2];
                if (ans < temp) ans = temp;
            }
            if (i+2 < n && j+1 < m) {
                int temp = a[i][j] + a[i+1][j] + a[i+2][j] + a[i+2][j+1];
                if (ans < temp) ans = temp;
            }
            if (i+1 < n && j+2 < m) {
                int temp = a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j];
                if (ans < temp) ans = temp;
            }
            if (i+2 < n && j+1 < m) {
                int temp = a[i][j] + a[i][j+1] + a[i+1][j+1] + a[i+2][j+1];
                if (ans < temp) ans = temp;
            }
            if (i+1 < n && j+1 < m) {
                int temp = a[i][j] + a[i][j+1] + a[i+1][j] + a[i+1][j+1];
                if (ans < temp) ans = temp;
            }
            if (i-1 >= 0 && j+2 < m) {
                int temp = a[i][j] + a[i][j+1] + a[i-1][j+1] + a[i-1][j+2];
                if (ans < temp) ans = temp;
            }
            if (i+2 < n && j+1 < m) {
                int temp = a[i][j] + a[i+1][j] + a[i+1][j+1] + a[i+2][j+1];
                if (ans < temp) ans = temp;
            }
            if (i+1 < n && j+2 < m) {
                int temp = a[i][j] + a[i][j+1] + a[i+1][j+1] + a[i+1][j+2];
                if (ans < temp) ans = temp;
            }
            if (i+2 < n && j-1 >= 0) {
                int temp = a[i][j] + a[i+1][j] + a[i+1][j-1] + a[i+2][j-1];
                if (ans < temp) ans = temp;
            }
            if (j+2 < m) {
                int temp = a[i][j] + a[i][j+1] + a[i][j+2];
                if (i-1 >= 0) {
                    int temp2 = temp + a[i-1][j+1];
                    if (ans < temp2) ans = temp2;
                }
                if (i+1 < n) {
                    int temp2 = temp + a[i+1][j+1];
                    if (ans < temp2) ans = temp2;
                }
            }
            if (i+2 < n) {
                int temp = a[i][j] + a[i+1][j] + a[i+2][j];
                if (j+1 < m) {
                    int temp2 = temp + a[i+1][j+1];
                    if (ans < temp2) ans = temp2;
                }
                if (j-1 >= 0) {
                    int temp2 = temp + a[i+1][j-1];
                    if (ans < temp2) ans = temp2;
                }
            }
        }
    }
    cout << ans << '\n';
    return 0;
}