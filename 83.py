# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        headSet = set()
        tmp = head
        while tmp.next != None:
            headSet.add(tmp.val)
            current = tmp
            while True:
                if tmp.next == None:
                    current.next = None
                    break
                elif tmp.next.val not in headSet:
                    current.next = tmp.next
                    tmp = tmp.next
                    break
                else:
                    tmp = tmp.next

        return head
