from collections import deque
class MyStack:
  def __init__(self):
    self.q = deque()

  def push(self, x):
    # 넣을 때마다 재정렬함으로 스택성질을 유지
    self.q.append(x)
    for _ in range(len(self.q)-1):
      self.q.append(self.q.popleft())
    
  def pop(self):
    return self.q.popleft()
  
  def top(self):
    return self.q[0]

  def empty(self):
    return len(self.q) == 0