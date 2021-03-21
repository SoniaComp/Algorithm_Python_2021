# 파이썬의 int(x, base=10) 함수는 진법 변환을 지원합니다.

'''
s = '가나다라'
n = 7

s.ljust(n) # 좌측 정렬
s.center(n) # 가운데 정렬
s.rjust(n) # 우측 정렬
'''


# 다른 언어에서는..(또는 이 기능을 모르시는 분은)
# 보통 사람들은 deep copy와 sort 함수를 이용합니다.
# ---
# 파이썬의 sorted를 사용해보세요. 반복문이나, deepcopy 함수를 사용하지 않아도 새로운 정렬된 리스트를 구할 수 있습니다.
'''
list1 = [3, 2, 1]
list2 = sorted(list1)
'''

# zip
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = [[], [], []]
for i in range(len(mylist)):
    for j in range(len(mylist[i])):
        new_list[i].append(mylist[j][i])

mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))
# zip(*iterables)는 각 iterables 의 요소들을 모으는 이터레이터를 만듭니다.
# 튜플의 이터레이터를 돌려주는데, i 번째 튜플은 각 인자로 전달된 시퀀스나 이터러블의 i 번째 요소를 포함합니다.
# 사용예 1: 여러개의 iterable 동시에 순회할 때
list1 = [1, 2, 3, 4]
list2 = [100, 120, 30, 300]
list3 = [392, 2, 33, 1]
answer = []
for number1, number2, number3 in zip(list1, list2, list3):
   print(number1 + number2 + number3)
# 사용 예 2: Key 리스트와 Value 리스트로 딕셔너리 생성하기
animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds)) # {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}

# 파이썬 파일 입출력 - with-as구문을 이용하여 더욱 간단하게
with open('myfile.txt') as file:
    for line in file.readlines():
        print(line.strip().split('\t'))

# 곱집합 구하기
import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
print(list(itertools.product(iterable1, iterable2, iterable3)))