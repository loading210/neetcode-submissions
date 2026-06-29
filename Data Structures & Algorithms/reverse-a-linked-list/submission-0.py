# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        l = ListNode(head.val)
        head = head.next
        while head != None:
            temp = ListNode()
            temp.val = head.val
            temp.next = l
            l = temp
            head = head.next
        return l

