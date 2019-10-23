// N, M 시리즈 문제
// 재귀함수
// 순열
// 비트마스트

// 1. 순서
// 2. 선택

// n과 m (1)
// 1부터 N까지 자연수 중에서 **중복없이 M개를 고른** 수열을 모두 구하는 문제
// 순서: 각각의 순서에 어디가 들어가는지 알아야 하기 때문에

// 일반화
// 인덱스 채우기
// 중복없이 : 어떤 수를 지금까지 사용했고, 어떤 수를 사용하지 않았는지
// true가 들어 있으면 i
// false가 들어있으면 사용하지 않는 것

// 방법 1
bool c[10];
int a[10];
void go(int index, int n, int m){
  if(index == m){ // index 번째를 채우려고 한다.
    // 수열을 출력
    return;
  }
  for(int i=1; i<=n; i++){
    if(c[i]) continue;
    c[i] = true;
    a[index] = i;
    go(index+1, n, m);
    c[i] = false;
  }
}