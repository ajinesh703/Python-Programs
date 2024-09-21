# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode):
        result = []
        
        # Helper function for recursion
        def inorder(node):
            if node is not None:
                inorder(node.left)  # Visit left subtree
                result.append(node.val)  # Visit the root
                inorder(node.right)  # Visit right subtree
        
        inorder(root)
        return result

# Example usage
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

solution = Solution()
print(solution.inorderTraversal(root))  # Output: [1, 3, 2]
