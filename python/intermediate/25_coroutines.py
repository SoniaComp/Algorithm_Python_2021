'''
generators are data producers
coroutines are data consumers
'''


'''
파이썬 generator, yield
함수로부터 만들어진 제너레이터 객체가 for 루프를 통해 처음 실행될 때 Python은 함수 내에 있는 코드를 yield 키워드를 만나기 전까지 실행하고 첫 번째 루프의 값을 반환하게 됩니다. 다음 루프 때에는 yield 키워드 뒤에 있는 코드를 실행하고 다시 루프를 돌면서 반환할 값이 아예 없을 때까지 계속 같은 과정을 반복하게 됩니다
https://tech.ssut.me/what-does-the-yield-keyword-do-in-python/

Coroutines consume values which are sent to it. A very basic example would be a grep alternative in Python:

http://www.dabeaz.com/coroutines/Coroutines.pdf
'''