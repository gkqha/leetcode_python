# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
#         if head == None:
#             return None
#         if m == n:
#             return head
#         node = head
#         start_pre = head
#         start = None
#         end = None
#         for i in range(1, n + 1):
#             print(i)
#             if i == m - 1:
#                 start_pre = node
#                 node = node.next
#             if i == m:
#                 start = node
#                 pre = node
#                 node = node.next
#             else:
#                 if i <= n and i > m:
#                     cur = node
#                     node.next = pre
#                     pre = node
#                     cur = cur.next
#                 if i == n + 1:
#                     start.next = cur
#                 else:
#                     node = node.next
#         return head
