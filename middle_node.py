def middle_node(self, head):
    length = 0
    current = head

    while current is not None:
        current = current.next
        length = length + 1

    if length == 1:
        return head

    middle = length // 2

    current_node = head
    count = 0

    while current_node is not None:
        current_node = current_node.next
        count = count + 1

        if count == middle:
            return current_node
