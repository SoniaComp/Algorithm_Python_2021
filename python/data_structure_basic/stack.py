# Python list 사용
class Stack_list(list): # 리스트를 상속받는다.
  push = list.append  # Insert
  # pop               # Delete - 내장 pop 메소드 활용

  def is_empty(self):
    if not self:
      return True
    else:
      return False
  
  def peek(self):
    return self[-1]

# Python Node 사용
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
  
class Stack:          # head만으로 구현이 가능하다.
  def __init__(self):
    self.head = None

  def is_empty(self):
    if not self.head:
      return True
    return False
  
  def push(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def pop(self):
    if self.is_empty():
      return None
    ret_data = self.head.data
    self.head = self.head.next
    return ret_data
  
  def peek(self):
    if self.is_empty():
      return None
    return self.head.data

# Python
# 내장된 메소드
# List: pop
# https://docs.python.org/ko/3/tutorial/datastructures.html

# Stack: __init__ -> head
# Node: __init__ -> data, next