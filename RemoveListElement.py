def removeListElement(head, val):
    # create a dummy node pointing next to head
    dummy = ListNode(next=head)
    # intialise prev to dummy and current node to head
    prev, curr = dummy, head

    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return dummy.next
