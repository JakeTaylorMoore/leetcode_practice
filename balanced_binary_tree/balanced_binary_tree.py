# Author:      Jacob Moore
# Date:        7/21/22
# Description: This program...
from structures import binary_search_tree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        # Find balance of left and right nodes
        L = self.balanceHelper(root.left)
        R = self.balanceHelper(root.right)
        # If -1, False
        if L == -1 or R == -1:
            return False
        elif abs(L - R) > 1:
            return False
        else:
            return True


    def balanceHelper(self, root):
        """
        recursively checks balance on each node
        :param root:
        :return: height
        """
        # Base case
        if root is None or root.val is None:
            return 0
        # Find balance of left and right nodes
        L = self.balanceHelper(root.left)
        R = self.balanceHelper(root.right)
        # If -1, False
        if L == -1 or R == -1:
            return -1
        elif abs(L - R) > 1:
            return -1
        else:
            return max(L, R) + 1


## More efficient solution from comments

# class Solution(object):
#     def isBalanced(self, root):

#         def check(root):
#             if root is None:
#                 return 0
#             left  = check(root.left)
#             right = check(root.right)
#             if left == -1 or right == -1 or abs(left - right) > 1:
#                 return -1
#             return 1 + max(left, right)

#         return check(root) != -1


def main():
    a = Solution()
    bst = binary_search_tree.BinarySearchTree()
    arr = [3,9,20,None,None,15,7]
    root = bst.create_bst(arr)
    print(a.isBalanced(root))

    arr = [1, 2, 2, 3, 3, None, None, 4, 4]
    root = bst.create_bst(arr)
    print(a.isBalanced(root))


if __name__ == "__main__":
    main()
