import collections

class TrieNode:
  def __init__(self):
    self.children = collections.defaultdict(TrieNode)
    self.word_id = -1
    self.palindrome_word_ids = []

class Trie:
  def __init__(self):
    self.root = TrieNode()
  
  @staticmethod
  def is_palindrome(word:str)-> bool:
    return word[::] == word[::-1]
  
  # 단어 삽입
  def insert(self, index, word) -> None:
    node = self.root
    for i, char in enumerate(reversed(word)):
      if self.is_palindrome(word[0:len(word)-i]):
        node.palindrome_word_ids.append(index)
      node = node.children[char]
      node.val = char
    node.word_id = index

  