# Author:      Jacob Moore
# Date:        7/26/22
# Description:
from structures import linked_list


class Solution(object):
    def reverseList(self, head, prev=None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            head.next = prev
            return head
        else:
            first = self.reverseList(head.next, head)
            head.next = prev
            return first


def main():
    a = Solution()

    ll = linked_list.LinkedList([1,2])
    head = a.reverseList(ll.getHead())
    arr = []
    while head is not None:
        arr.append(head.val)
        head = head.next
    print(arr)

    ll = linked_list.LinkedList([1,2,3,4,5])
    head = a.reverseList(ll.getHead())
    arr = []
    while head is not None:
        arr.append(head.val)
        head = head.next
    print(arr)

    ll = linked_list.LinkedList([])
    head = a.reverseList(ll.getHead())
    arr = []
    while head is not None:
        arr.append(head.val)
        head = head.next
    print(arr)


if __name__ == '__main__':
    main()
