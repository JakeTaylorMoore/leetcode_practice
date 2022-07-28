# Author:      Jacob Moore
# Date:        7/28/22
# Description: Leetcode #543. All work is original. Faster than 97% of submissions
from structures import binary_search_tree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def helper(root):
            if root is None:
                return 0, 0
            ld, ltot = helper(root.left)
            rd, rtot = helper(root.right)
            total = max(ltot, rtot, (ld + rd))
            return max(1 + ld, 1 + rd), total

        a, total = helper(root)
        return total


def main():
    a = Solution()
    bst = binary_search_tree.BinarySearchTree().create_bst([1,2,3,4,5])
    print(a.diameterOfBinaryTree(bst))

    bst = binary_search_tree.BinarySearchTree().create_bst([1,2])
    print(a.diameterOfBinaryTree(bst))


if __name__ == '__main__':
    main()
