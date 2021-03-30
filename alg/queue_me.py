class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class MyCircularDeque:
  def __init__(self, k: int):
    self.head, self.tail = ListNode(None), ListNode(None)
    self.k, self.len = k, 0 # 최대 길이
    self.head.right, self.tail.left = self.tail, self.head

  # 이중 연결 리스트에 신규 노드 삽입
  def _add(self, node:ListNode, new:ListNode):
    # node new node.right[n]
    n = node.right # 노드 뒤에 삽입
    node.right = new 
    new.left, new.right = node, n
    n.left = new

  def _del(self, node: ListNode):
    # node node.right node.right.right
    # node node.right.right
    n = node.right.right
    node.right = n
    n.left = node

  def insertFront(self, value: int) -> bool:
    if self.len == self.k:
      return False
    self.len += 1
    self._add(self.head, ListNode(value))
    return True
  
  def insertLast(self, value: int) -> bool:
    if self.len == self.k:
      return False
    self.len += 1
    self._add(self.tail.left, ListNode(value))
