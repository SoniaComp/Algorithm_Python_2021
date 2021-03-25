''' 
파이썬 다운 방식 -> 파이썬의 기본 기능을 이용하면 단 한줄로 쉽게 풀이할 수 있다.
'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        ''' 풀이 1
        for idx in range(len(s)//2):
            s[idx], s[len(s)-1-idx] = s[len(s)-1-idx] , s[idx]
        '''
        ''' 풀이 2: 파이썬 다운 방식
        s.revrse()
        '''
        '''투포인터
        '''
        left, right = 0, len(s)-1
        while left < right: # 투 포인터인경우에는 left, right로 크기 비교로 크로스 되는 걸 막는다.
          s[left], s[right] = s[right], s[left]
          left += 1
          right -= 1
          left, right = 0, len(s)-1
            # 투 포인터가 수학 연산 과정이 없어서 빠르다.

'''
reversed(seq)
Return a reverse iterator. seq must be an object which has a __reversed__() method or supports the sequence protocol (the __len__() method and the __getitem__() method with integer arguments starting at 0).

reverse는 값을 반환하지 않고, 단순히 해당 list를 뒤섞어준다.
-> .sort()와 같은 원리

reversed는 내장함수로, list에서 제공하는 함수가 아니다.
-> ‘reversed’ 객체를 반환한다.
-> reversed 객체를 tuple 혹은 list로 바꾸어 사용해주려면 다음과 같이 하면 된다.
l = ['a', 'b', 'c']
t = ('a', 'b', 'c')
list(reversed(l))  # ['c', 'b', 'a']
tuple(reversed(t))  # ('c', 'b', 'a')
'''