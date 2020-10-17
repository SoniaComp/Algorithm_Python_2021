import pytest


class Node:
    def __init__(self, element):
        self.element = element
        self.next = None


class MyCircularDeque:

    def __init__(self, k: int):
        self.head = Node('head')
        self.max_count = k
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        cur_front = self.head.next
        self.head.next = Node(value)
        self.head.next.next = cur_front
        self.size += 1
        return True

    def findNode(self, value: int, order) -> Node:
        cur = self.head
        for _ in range(order):
            cur = cur.next
        return cur

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        cur = findNode(value, self.size)
        cur.next = Node(value)
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        new_first = self.head.next.next
        self.haed.next = new_first
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        prev = findNode(self.size-1)
        prev.next = None
        self.size -= 1
        return True

    def getFront(self) -> int:
        return self.head.next.element

    def getRear(self) -> int:
        return self.last.element

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.size == self.max_count:
            return True
        return False


@pytest.mark.parametrize(
    "commands", "params"
    [
        ["MyCircularDeque", "insertFront", "getRear", "deleteLast", "getRear", "insertFront", "insertFront", "insertFront", "insertFront", "isFull", "insertFront", "isFull", "getRear", "deleteLast", "getFront", "getFront", "insertLast", "deleteFront", "getFront", "insertLast", "getRear", "insertLast", "getRear", "getFront", "getFront", "getFront", "getRear", "getRear", "insertFront", "getFront", "getFront", "getFront", "getFront", "deleteFront", "insertFront", "getFront", "deleteLast", "insertLast", "insertLast", "getRear", "getRear", "getRear", "isEmpty", "insertFront", "deleteLast", "getFront", "deleteLast", "getRear", "getFront", "isFull", "isFull",
            "deleteFront", "getFront", "deleteLast", "getRear", "insertFront", "getFront", "insertFront", "insertFront", "getRear", "isFull", "getFront", "getFront", "insertFront", "insertLast", "getRear", "getRear", "deleteLast", "insertFront", "getRear", "insertLast", "getFront", "getFront", "getFront", "getRear", "insertFront", "isEmpty", "getFront", "getFront", "insertFront", "deleteFront", "insertFront", "deleteLast", "getFront", "getRear", "getFront", "insertFront", "getFront", "deleteFront", "insertFront", "isEmpty", "getRear", "getRear", "getRear", "getRear", "deleteFront", "getRear", "isEmpty", "deleteFront", "insertFront", "insertLast", "deleteLast"]
        [[77], [89], [], [], [], [19], [23], [23], [82], [], [45], [], [], [], [], [], [74], [], [], [98], [], [99], [], [], [], [], [], [], [8], [], [], [], [], [], [75], [], [], [35], [59], [], [], [], [], [22], [], [], [], [], [], [], [], [
        ], [], [], [], [21], [], [26], [63], [], [], [], [], [87], [76], [], [], [], [26], [], [67], [], [], [], [], [36], [], [], [], [72], [], [87], [], [], [], [], [85], [], [], [91], [], [], [], [], [], [], [], [], [], [34], [44], []]
    ]
)
def test_solution(commands, params):
    pass


'''
["MyCircularDeque","insertFront","getRear","deleteLast","getRear","insertFront","insertFront","insertFront","insertFront","isFull","insertFront","isFull","getRear","deleteLast","getFront","getFront","insertLast","deleteFront","getFront","insertLast","getRear","insertLast","getRear","getFront","getFront","getFront","getRear","getRear","insertFront","getFront","getFront","getFront","getFront","deleteFront","insertFront","getFront","deleteLast","insertLast","insertLast","getRear","getRear","getRear","isEmpty","insertFront","deleteLast","getFront","deleteLast","getRear","getFront","isFull","isFull","deleteFront","getFront","deleteLast","getRear","insertFront","getFront","insertFront","insertFront","getRear","isFull","getFront","getFront","insertFront","insertLast","getRear","getRear","deleteLast","insertFront","getRear","insertLast","getFront","getFront","getFront","getRear","insertFront","isEmpty","getFront","getFront","insertFront","deleteFront","insertFront","deleteLast","getFront","getRear","getFront","insertFront","getFront","deleteFront","insertFront","isEmpty","getRear","getRear","getRear","getRear","deleteFront","getRear","isEmpty","deleteFront","insertFront","insertLast","deleteLast"]
[[77],[89],[],[],[],[19],[23],[23],[82],[],[45],[],[],[],[],[],[74],[],[],[98],[],[99],[],[],[],[],[],[],[8],[],[],[],[],[],[75],[],[],[35],[59],[],[],[],[],[22],[],[],[],[],[],[],[],[],[],[],[],[21],[],[26],[63],[],[],[],[],[87],[76],[],[],[],[26],[],[67],[],[],[],[],[36],[],[],[],[72],[],[87],[],[],[],[],[85],[],[],[91],[],[],[],[],[],[],[],[],[],[34],[44],[]]
  '''
