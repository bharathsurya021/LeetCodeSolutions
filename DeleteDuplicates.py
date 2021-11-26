# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    while curr and curr.next:
        if curr.next and curr.next.val == curr.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head
