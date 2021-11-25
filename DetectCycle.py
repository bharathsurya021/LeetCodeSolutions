def detectCycle(head):
    current = head
    mySet = set()
    while current:
        if current in mySet:
            return True
        mySet.add(current)
        current = current.next
    return False


# O(1) space


def detectCycle1(head):
    current = rapidCurrent = head
    while current and rapidCurrent and rapidCurrent.next:
        current = current.next
        rapidCurrent = rapidCurrent.next.next
        if current == rapidCurrent:
            return True
    return False
