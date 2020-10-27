'''
'이진 트리' 데이터 구조는 논리적인 구조다. 이를 파일이나 디스크에 저장하기 위해서는 물리적인 형태로 바꿔줘야 한다. -> 직렬화
파이썬 직렬화 모듈: pickle
pickling : 파이썬 객체의 계층 구조를 바이트 스트림으로 변경하는 작업
BFS 탐색
노드가 존재하지 않을 경우, 널이라는 의미로 '#'을 추가한다.
'''
# Definition for a binary tree node.

import collections; 

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = collections.deque([root])
        result = ['#']
        # 트리 BFS 직렬화
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                
                result.append(str(node.val))
            else:
                result.append('#')
            return ' '.join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '# #':
            return None
        
        nodes = data.split()
        
        # init
        root = TreeNode(int(nodes[1]))
        
        queue = collections.deque([root])
        index = 2
        
        # 빠른 런너처럼 자식 노드 결과를 먼저 확인 후 큐 삽입
        while queue:
            node = queue.popleft()
            if index >= len(nodes):
                break
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1
            
            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index+=1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))