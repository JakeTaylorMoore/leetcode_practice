# Author:      Jacob Moore
# Date:        7/14/22
# Description: I wrote this program to solve the leetcode problem invert binary tree # 226
#              I copied the binary tree configuration code from:
#              https://www.geeksforgeeks.org/construct-complete-binary-tree-given-array/

# Function to insert nodes in level order
def insertLevelOrder(arr, i, n):
    root = None
    # Base case for recursion
    if i < n:
        root = TreeNode(arr[i])

        # insert left child
        root.left = insertLevelOrder(arr, 2 * i + 1, n)

        # insert right child
        root.right = insertLevelOrder(arr, 2 * i + 2, n)

    return root


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        if root.left is not None:
            self.invertTree(root.left)
        if root.right is not None:
            self.invertTree(root.right)
        extra = root.left
        root.left = root.right
        root.right = extra
        return root

def main():
    a = Solution()
    arr = [4,2,7,1,3,6,9]
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, 0, n)
    print(a.invertTree(root))

    arr = [2, 1, 3]
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, 0, n)
    a.invertTree(root)

    arr = []
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, 0, n)
    a.invertTree(root)


if __name__ == "__main__":
    main()