from collections import defaultdict

# Definition for singly-linked list
class ListNode:
  def __init__(self, key=None, value=None):
    self.key = key
    self.value = value
    self.next = None

class MyHashMap:
  def __init__(self):
    self.size = 1000
    self.table = defaultdict(ListNode) # key(index) 값이 없을 경우 value는 ListNode 
    # 위에서 정의한, key, value랑 다르다.
    # defaultdict: key값이 없을 경우 미리 지정해 놓은 초기(default)값을 반환하는 dictionary이다.

  # 삽입
  def put(self, key: int, value: int) -> None:
    index = key % self.size
    # 인덱스에 노드가 없다면 삽입 후 종료
    if self.table[index].value is None: # defaultdict 특
      self.table[index] = ListNode(key, value)
      return
    
    # 인덱스에 노드가 존재하는 경우 연결리스트 처리
    p = self.table[index]
    while p: # 마지막 노드로 이동
      if p.key == key:
        p.value = value
        return
      if p.next is None:
        break
      p = p.next
    p.next = ListNode(key, value)

    # 조회
    def get(self, key: int) -> int:
      index = key % self.size
      if self.table[index].value is None:
        return -1
      
      # 노드가 존재할 때 일치하는 키 탐색
      p = self.table[index]
      while p:
        if p.key == key:
          return p.value
        p = p.next
      return -1

    # 삭제
    def remove(self, key: int) -> None:
      index = key % self.size
      if self.table[index].value is None:
        return
    
      # 인덱스의 첫번째 노드일 때 삭제 처리
      p = self.table[index]
      if p.key == key:
        self.table[index] = ListNode() if p.next is None else p.next
      
      # 연결리스트 노드 삭제
      prev = p
      while p:
        if p.key == key:
          prev.next = p.next
          return
        prev, p = p, p.next # p는 이동
        