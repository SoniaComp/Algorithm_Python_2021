# 직접적이 인덱스 접근이 어려움
class ListNode:
    def __init__(self, index, next_distance=0):
        self.index = index
        self.next = None
        self.next_distance = next_distance
        self.check = False

def solution(n, weak, dist):    
    if len(weak) == 1:
        return 1
    answer = ''
    # 외벽 만들기
    head = prev = ListNode(weak[0])
    for w_idx in weak[1:-1]:
        dist = w_idx - prev.index
        cur = ListNode(w_idx, dist)
        prev.next = cur
        prev = cur
    # 마지막
    dist = (12-weak[-1]) + weak[0]
    tail = ListNode(weak[-1], dist)
    tail.next = head
    
    # 점검 할 수 있는 거 체크
    count = 0
    
    return answer