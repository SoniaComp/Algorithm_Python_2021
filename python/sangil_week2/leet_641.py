class MyCircularDeque:
    
    def __init__(self, k: int):
        self.deque = []
        self.max_count = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque.extend([self.getRear()])
        for idx, _ in reversed(list(enumerate(self.deque))):
            if idx == len(self.deque)-1:
                continue
            self.deque[idx+1] = self.deque[idx]
        self.deque[0] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque.append(value)
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        for idx, _ in reversed(list(enumerate(self.deque))):
            if idx == len(self.deque)-1:
                continue
            self.deque[idx] = self.deque[idx+1]
        self.deque.pop()
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.deque.pop()
        return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[0]

    def getRear(self) -> int:
          if self.isEmpty():
            return -1
          return self.deque[len(self.deque)-1]

    def isEmpty(self) -> bool:
          if len(self.deque):
            return False
          return True
        

    def isFull(self) -> bool:
          if len(self.deque) == self.max_count:
            return True
          return False
        
  '''
  오류 케이스
["MyCircularDeque","insertFront","getRear","deleteLast","getRear","insertFront","insertFront","insertFront","insertFront","isFull","insertFront","isFull","getRear","deleteLast","getFront","getFront","insertLast","deleteFront","getFront","insertLast","getRear","insertLast","getRear","getFront","getFront","getFront","getRear","getRear","insertFront","getFront","getFront","getFront","getFront","deleteFront","insertFront","getFront","deleteLast","insertLast","insertLast","getRear","getRear","getRear","isEmpty","insertFront","deleteLast","getFront","deleteLast","getRear","getFront","isFull","isFull","deleteFront","getFront","deleteLast","getRear","insertFront","getFront","insertFront","insertFront","getRear","isFull","getFront","getFront","insertFront","insertLast","getRear","getRear","deleteLast","insertFront","getRear","insertLast","getFront","getFront","getFront","getRear","insertFront","isEmpty","getFront","getFront","insertFront","deleteFront","insertFront","deleteLast","getFront","getRear","getFront","insertFront","getFront","deleteFront","insertFront","isEmpty","getRear","getRear","getRear","getRear","deleteFront","getRear","isEmpty","deleteFront","insertFront","insertLast","deleteLast"]
[[77],[89],[],[],[],[19],[23],[23],[82],[],[45],[],[],[],[],[],[74],[],[],[98],[],[99],[],[],[],[],[],[],[8],[],[],[],[],[],[75],[],[],[35],[59],[],[],[],[],[22],[],[],[],[],[],[],[],[],[],[],[],[21],[],[26],[63],[],[],[],[],[87],[76],[],[],[],[26],[],[67],[],[],[],[],[36],[],[],[],[72],[],[87],[],[],[],[],[85],[],[],[91],[],[],[],[],[],[],[],[],[],[34],[44],[]]
  '''