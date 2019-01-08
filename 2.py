# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r = ListNode(0)
        res = r
        car = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = car + x + y
            res.next = ListNode(s % 10)
            car = s // 10
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
            res = res.next
        if car > 0:
            res.next = ListNode(1)
        return r.next
