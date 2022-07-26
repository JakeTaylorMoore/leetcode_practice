# Author:      Jacob Moore
# Date:        7/23/22
# Description: This program...


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList(object):
    def __init__(self, array):

        def CreateList(arr):
            """
            Create linked list from array
            :param arr:
            :return LinkedList:
            """
            if not arr:
                return None
            head = ListNode(arr[0])
            temp = head
            for i in range(1, len(arr)):
                node = ListNode(arr[i])
                temp.next = node
                temp = temp.next
            return head

        self.head = CreateList(array)

    def getHead(self):
        return self.head

    def createCycle(self, pos):
        """
        Takes in the position the cycle returns to and adds a
        cycle to the list
        :param pos:
        :return:
        """
        node = self.head
        while node.next is not None:
            node = node.next
        temp_node = self.head
        for i in range(pos):
            temp_node = temp_node.next
        node.next = temp_node
        return
