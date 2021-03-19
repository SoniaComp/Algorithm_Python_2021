from functools import cmp_to_key
from operator import itemgetter

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        print('{} {}'.format(name, score))

    @staticmethod        
    def comparator(a, b):
        return b.score - a.score if b.score != a.score else -1 if a.name < b.name else 1
        # + 면 바꾸는 연산 수행 / - 면 바꾸는 연산 수행하지 않음 comparator
        # cmp_to_key : 두 값의 조건에 따라 비교하기
        # sorted: https://docs.python.org/ko/3/howto/sorting.html
        # comparator: https://blackinkgj.github.io/python-custom-comparator/

n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)