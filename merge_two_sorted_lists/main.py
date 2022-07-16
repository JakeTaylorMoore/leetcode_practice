# Author:      Jacob Moore
# Date:        6/25/22
# Description: Leetcode question #21 merge two sorted lists
#              Solution used: https://leetcode.com/problems/merge-two-sorted-lists/discuss/1826693/Python3-MERGING-Explained

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # cur points to current node, dummy points to beginning
        cur = dummy = ListNode()
        # While both node objects exist
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                # list1 object now becomes current list1.next value to iterate
                cur = list1
                list1 = list1.next
                # Now cur can be set to list1
                # cur = list1
            else:
                cur.next = list2
                cur = list2
                list2 = list2.next
                # cur = list2

        # If one is empty and the other is not
        if list1 or list2:
            cur.next = list1 if list1 else list2

        # Since dummy.val is 0 and .next is either the sorted list or None
        return dummy.next


def main():
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    test = Solution()
    test.mergeTwoLists(list1, list2)

if __name__ == '__main__':
    main()
