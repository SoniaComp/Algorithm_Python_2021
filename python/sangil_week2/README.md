### 1. dictionary
* dictionary에서 key 값 확인: x in dict
* dictionary에 기본 값으로 초기화: defaultdict(초기값설정 함수) ex) dafaultdict(int) => 기본값 0 / defaultdict(list)

### 2. zip()
```Python
ys = list(zip(*xs))
xs = list(zip(*ys))
# zip의 input과 Output은 대칭을 이룬다.
```

cf. zip이 iterable한 객체를 리턴 하는 이유
- 200만개가 되는 엄청나게 긴 경우, 객체가 아닌 결과 값을 또 리턴하게 되면 새로운 메모리 할당이 발생해서 --> 메모리 초과하는 문제 발생
- 그래서 바로 처리하지 않고, 값을 요청할 때 처리.. lazy한 처리
- 따라서 iterate한 객체는 list를 만들어서 돌리는 것보다는 객체 자체에 접근해서 돌아가는 게 낫다. 
ex) for i in list(x): ~
--> 이것보다는 enumerate나.. 등등..

### 3. iterable한 객체를 도는 iterator

```python
it = iter(xs) # iterator 선언

print(it[0]) # error
# 특정 인덱스에 바로 접근 불가능

for x in it:
  print(x) 
  # 최초 한번은 순회
  # 두번째 실행부터는 순회가 이미 끝나서 안됨
  # 실무 tip: 큰 데이터 set을 순차적으로 읽어 나갈 때 사용. ex) 10GB 데이터를 순차적으로 접근할 때 -> 만약에 다시 메모리 올려놔서 접근하려고 하면, 메모리 터짐 / 파일을 쭉 읽으면서 필요 없는 데이터 정리하고 싶을 때
  # 하지만 왔다갔다 하거나, 특정 1개 다이렉트 할 경우는 적절하지 않음

# iterator 접근할 때 Next로 접근
try: 
  x = next(it)
  print(x)
except stopIteration:
  break
```

### 4. 아스테리스크
* 가변 인자: 여러개를 받아야 할 때 -> tuple로 풀어준다.
함수 내에서는 튜플을 묶을 때, 여러개를 묶어줄 때 사용한다.

### 5. tee


### 6. Python Code Style
1. _ 변수 -> 신경 쓰지 않아도 된다라는 것을 명시적으로 표현한 것
2. combination 라이브러리를 쓰면 읽기가 편해짐
3. 파이썬이 기피하는 코드 스타일
```python
for i in range(len(xs)):
  # 이렇게 인덱스로 직접 접근하는 건 파이썬이 기피하는 스타일
  # 인덱스로 접근해서 뭐든 할 수 있다.. 이렇게 뭐든 할 수 있는 코드는 보기가 어렵다.

# 좋은 코드 스타일은 기능을 제한하고, 코드의 가독성을 높인다.
for x, _ in enumerate(xs):
  # index 값은 사용하지 않고, 직접 그 값만 사용한다는 것을 알 수 있다.
```


### 기타
* 크롤링, 덤프, RestAPI
* 코드는 재활용하자! --> 괜찮은 코드 utils 폴더에 라이브러리화