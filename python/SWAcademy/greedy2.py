class BabyJin:
    def __init__(self):
        self.cards={}
    
    def add_and_result(self, card):
        cards = self.cards
        if card in cards: # 받은 카드가 기존에 있을 때 triplet 찾기
            cards[card] += 1
            if cards[card] >= 3: # triplet
                return True
            
        else: # 받은 카드가 기존에 없을 때 run 찾아보기
            cards[card] = 1
            if card - 1 in cards: 
                if card - 2 in cards or card + 1 in cards:
                    return True # run (-2, -1) or (-1, +1)
            elif card + 1 in cards and card + 2 in cards:
                return True # run (+1, +2)
        return False # 결과 안남

T = int(input())
for test_case in range(1, T + 1):
    p1 = BabyJin()
    p2 = BabyJin()
    lst = list(map(int, input().split()))
    result = 0
    for i in range(len(lst)):
        # 짝수번째 카드는 p1에게 주고 게임이 끝나면
        if i % 2 == 0 and p1.add_and_result(lst[i]):
            result = 1
            break
        # 홀수번째 카드는 p2에게 주고 게임이 끝나면
        if i % 2 == 1 and p2.add_and_result(lst[i]):
            result = 2
            break
    print('#{} {}'.format(test_case, result))