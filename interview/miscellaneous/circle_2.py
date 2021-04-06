class Node:
  def __init__(self, data):
    self.data = data
    self.parent = self
    self.rank = 1
    self.count = 1

def find_parent(node):
  if node.parent is node:
    return node
  return find_parent(node.parent)

def union_nodes(n1, n2):
  if n1 is n2:
    return n1
  p1, p2 = find_parent(n1), find_parent(n2)

  if p1 is p2:
    return p1
  if p1.rank < p2.rank:
    p1, p2 = p2, p1
  p2.parent = p1 
  if p1.rank == p2.rank:
    p1.rank += 1
  p1.count += p2.count
  return p1