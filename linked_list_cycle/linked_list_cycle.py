# Author:      Jacob Moore
# Date:        7/23/22
# Description: This program...

# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached
# again by continuously following the next pointer. Internally, pos is used to denote the
# index of the node that tail's next pointer is connected to. Note that pos is not passed
# as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.
from structures import linked_list


# Solution utilizes exception. From: https://leetcode.com/problems/linked-list-cycle/discuss/44494/Except-ionally-fast-Python
class Solution(object):
    def hasCycle(self, head):
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False


## My solution attempt. Only works if list only has unique values
# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         node = head
#         arr = []
#         while node is not None:
#             if node.val in arr:
#                 return True
#             arr.append(node.val)
#             node = node.next
#         return False


def main():
    a = Solution()
    arr = [3,2,0,-4]
    pos = 1
    new_list = linked_list.LinkedList(arr)
    new_list.createCycle(pos)
    head = new_list.getHead()
    print(a.hasCycle(head))



if __name__ == "__main__":
    main()