# Author:      Jacob Moore
# Date:        7/20/22
# Description: This program is my solution to leetcode #235 lowest common ancestor of a binary search tree
from structures import binary_search_tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # If both are larger than current root, recur to the right
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # If both are smaller, recur left
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # Otherwise, current root is your answer. It is either equal to p or q or their lca
        else:
            return root


def main():
    a = Solution()
    arr = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    bst = binary_search_tree.BinarySearchTree()
    root = bst.create_bst(arr)
    p = bst.get_node(root, 2)
    q = bst.get_node(root, 8)
    answer = a.lowestCommonAncestor(root, p, q)
    print(answer.val)




if __name__ == "__main__":
    main()
