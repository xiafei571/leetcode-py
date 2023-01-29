# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
       
        curDepth = 0
        # {node.val, (parent, depth)}
        nodeDict = {}
        nodeDict[root.val] = (None, curDepth) 
        queue = collections.deque([root])

        while queue:
            curDepth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    nodeDict[node.left.val] = (node.val, curDepth)
                if node.right:
                    queue.append(node.right)
                    nodeDict[node.right.val] = (node.val, curDepth)
                
        return nodeDict[x][0] != nodeDict[y][0] and nodeDict[x][1] == nodeDict[y][1]