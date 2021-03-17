from collections import deque

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = deque([root])

        while queue:
            node = queue.popelft() # node.stack.pop() stack으로 수정하면 dfs

            # 부모노드로부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)
                # stack일 경우 후위 순회 방식
                # stack.append(node.left)
                # stack.append(node.right)
                # node.left, node.right = node.right, node.left
        return root