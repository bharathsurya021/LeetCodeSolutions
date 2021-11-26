# T(O(n)),S(O(1))
def reverseList(head):
    prev, curr = None, head

    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    return prev


# T(O(n)),S(O(n))-->recursive
def reverseList1(self, head):
    if not head:
        return None

    newHead = head
    if head.next:
        newHead = self.reverseList1(head.next)
        head.next.next = head
    head.next = None
    return newHead
