'''
이진 트리 데이터 구조는 논리적인 구조다.
이를 파일이나 디스크에 저장하기 위해서는 물리적인 형태로 바꿔줘야 하는데, 이를 직렬화(Serialize)라고 한다. 
반대는 역직렬화(Deserialize)
파이썬에는 pickle이라는 직렬화 모듈을 기본으로 제공한다. 이 모듈의 이름으로 인해, 파이썬 객체의 계층(Hierarchy) 구조를
바이트 스트림(Byte Stream)으로 변경하는 작업을 피클링(Pickling)이라고 한다. -> 마샬링(Marshalling), 플래트닝
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = deque([root])
        result = ['#']
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
        
        root = TreeNode(int(nodes[1]))
        queue = deque([root])
        index = 2
        # 빠른 러너처럼 자식 노드 결과를 먼저 확인 후 큐 삽입
        while queue:
            node = queue.popleft()
            #left
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1
            # right
            if nodes[index] is not '#':
                nodes.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))