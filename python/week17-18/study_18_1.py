# 1차원 배열과 2차원 배열
# mutable 가변 객체와 immutable 불변 객체
pattern_size = 7
[[0] for i in range(pattern_size)] # 2차원 배열은 deep copy, shallow copy 문제로 이렇게 하는게 좋다.

# 라빈 카프 알고리즘
# 해시
# d = 256 / % q = 10007
# 나누기 값을 안해주면, 파이썬은 오버플로우 문제 없이 값을 있는 그대로 다 들고 있기 떄문에 너무 많다.
# q는 primenumber에서 선택
# 충돌이 최대한 적으면서도 효율적으로

# DP 풀때
# 2차원 배열을 하는 것도 좋지만
# arr 2개를 하면서 나아가기
# N^2 공간복잡도가 N으로 준다! 
# 메모리 적게 쓰면 대체로 속도가 줄어든다.
# 시간 복잡도는 그대로

# 파이썬 
# 파이썬_어노테이션
# 파이썬_데코레이터
'''
- https://wiki.python.org/moin/PythonDecorators
- 
A decorator is the name used for a software design pattern. Decorators dynamically alter the functionality of a function, method, or class without having to directly use subclasses or change the source code of the function being decorated.
- static method
self를 안받음. 전역변수를 안쓰는 점이 좋음. OO의 관점에서.
네임스페이스 관점에서 그냥 함수보다 클래스 안에 이 데코레이터를 사용해서 하는 것이 좋은 것 같다는 의견.
- class method
클래스 자체를 넘길 때


파이썬 데코레이터 어노테이션은 아직 잘 모르겠다.
좀 더 공부해야겠다.
'''

# 파이썬 클린 코드
'''
이것도 현업에서 중요한 문제.
for 문안에 또 for문... 그렇게 하는 것보다
문제를 생각해보면
예를 들어 무지의 먹방 라이브
- 선형으로 바꿔서 시간복잡도를 줄이는 것도 좋지만
- 문제 자체를 분석해서,
- 여러개를 한꺼번에 빼버리는, 과정 자체를 생략할 수 있게 하는 함수를 짜서
- 하나의 함수는 하나의 행위만 담당하고
- 이런 클린 코드를 짜는 것도 중요

재밌당
'''