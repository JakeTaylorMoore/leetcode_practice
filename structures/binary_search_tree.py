# Author:      Jacob Moore
# Date:        7/21/22
# Description: This program is an implementation of a binary search tree to use for leetcode problems
#              I copied the binary tree configuration code from:
#              https://www.geeksforgeeks.org/construct-complete-binary-tree-given-array/


class BinarySearchTree(object):
    # Function to insert nodes in level order
    def insertLevelOrder(self, arr, i, n):
        root = None
        # Base case for recursion
        if i < n:
            root = TreeNode(arr[i])

            # insert left child
            root.left = self.insertLevelOrder(arr, 2 * i + 1, n)

            # insert right child
            root.right = self.insertLevelOrder(arr, 2 * i + 2, n)

        return root


    def create_bst(self, arr):
        """
        Takes in array and returns root node of created bst
        :param arr:
        :return: root node
        """
        return self.insertLevelOrder(arr, 0, len(arr))

    def get_node(self, root, val):
        """
        Takes in a numerical value and returns the actual node that matches the value if it is in the bst
        :param root:
        :param val:
        :return: node
        """
        if root is None:
            return None
        elif root.val == val:
            return root
        elif val > root.val:
            return self.get_node(root.right, val)
        else:
            return self.get_node(root.left, val)


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

