# Python list 사용
class Queue_list(list): # 리스트를 상속받는다.
  enqueue = list.append  # Insert

  def dequeue(self):
    return self.pop(0)

  def is_empty(self):
    if not self:
      return True
    else:
      return False
  
  def peek(self):
    return self[0]

# Python Node 사용
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
  
class Stack:          # head, tail
  def __init__(self):
    self.head = None
    self.tail = None

  def is_empty(self):
    if not self.head:
      return True
    return False
  
  def enqueue(self, data):
    new_node = Node(data)

    if self.is_empty():
      self.head = new_node
      self.tail = new_node
      return

    self.tail.next = new_node
    self.tail = new_node

  def dequeue(self):
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

# Queue: __init__ -> head, tail
# Node: __init__ -> data, next