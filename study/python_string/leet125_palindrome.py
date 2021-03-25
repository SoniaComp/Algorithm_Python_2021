import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() # 아래 식에 다음 연산이 포함되어 있다. .replace(' ', '')
        s = re.sub('[^a-z0-9]', '', s) 
        return s == s[::-1]
    # isalnum() : 영문자, 숫자 여부를 판별하는 함수
    
'''파이썬 문자열 슬라이싱
파이썬에서 문자열 슬라이싱이라는 매우 편리한 기능을 제공한다. 무엇보다 내부적으로 매우 빠르게 동작한다.
위치를 지정하면 해당 위치의 """"배열 포인터""""를 얻게 되며 이를 통해 연결된 객체를 찾아 실제 값을 찾아내는데, 
이 과정은 매우 빠르게 진행되므로 문자열을 조작할 때 항상 슬라이싱을 우선으로 사용하는 편이 속도 개선에 유리하다.

[:] 문자열이나 리스트를 복사하는 파이선 다운 방식
'''