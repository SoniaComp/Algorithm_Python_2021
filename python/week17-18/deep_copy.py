'''
파이썬 객체에는 mutable 과 immutable 객체가 있습니다.

mutable한 객체는할당하면, 값이 할당되는 것이 아닌 메모리 주소를 바라봅니다.
변경하면, 모두 바뀜
- b에 a를 할당하면, 값이 할당되는 것이 아니라 같은 메모리 주소를 바라봅니다.
- b를 변경하면 같이 a도 바뀝니다.

immutable한 객체는 할당하면, 역시 같은 메모리 주소를 바라보지만, 
다른 값을 할당하면, 재할당이 이루어지며 메모리 주소가 변경됩니다.
'''
# 참조: https://wikidocs.net/16038

# 얕은 복사
# 슬라이싱으로 할당하면 새로운 아이디가 부여되지만, 
# mutable안의 mutable은 같은 값을 참조하게 되어, 서로 영향을 받는다.
a = [1,2,3]
b = a[:]
# b = copy.copy(a)
print(id(a))
print(id(b))
a==b
a is b
b[0] = 5
print(a)
print(b)

# 깊은 복사
# 내부에 있는 객체들까지 모두 새롭게 copy되어 mutable 객체의 위와 같은 문제를 해결한다.
import copy
a = [[1,2], [3,4]]
b = copy.deepcopy(a)
a[1].append(5)
print(a)
print(b)
