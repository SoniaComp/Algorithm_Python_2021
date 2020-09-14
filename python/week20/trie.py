'''
트라이는 보통 prefix tree, digital search tree, retrieval tree라고도 부른다. 트라이는 문자열을 key로 사용하는 동적인 set 또는 연관 배열을 저장하는 트리의 확장된 자료구조이다.
'''
class Node(object):
  def __init__(self, key, data=None):
    self.key = key
    self.data = data
    self.children = {}

class Trie(object):
  def __init__(self):
    self.head = Node(None)

  def insert(self, string):
    curr_node = self.head

    for char in string:
      if char not in curr_node.children:
        curr_node.children[char] = Node(char)
      curr_node = curr_node.children[char]

  def search(self, string):
    curr_node = self.head

    for char in string:
      if char in curr_node.children:
        curr_node = curr_node.children[char]
      else:
        return False
      
    return True
  
  def starts_with(self, prefix):
    curr_node = self.head
    result = []
    subtrie= None

    for char in prefix:
      if char in curr_node.children:
        curr_node = curr_node.children[char]
        subtrie = curr_node
      else:
        return None
      
      queue = list(subtrie.children.values())

      while queue:
        curr = queue.pop()
        if curr.data != None:
          result.append(curr.data)

        queue+= list(curr.children.values())

      return result