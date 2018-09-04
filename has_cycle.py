# Given a linked list, determine if it has a cycle in it.


def has_cycle(head):
    ll_set = set()
    current = head

    while current:
        if current not in ll_set:
            ll_set.add(current)
            current = current.next
        else:
            return True
    return False
