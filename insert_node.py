def insert_node(head, data, position):
    current = head
    place = 0

    if place == position:
        self.head = Node(data)
        self.head.next = current

    while current.next is not None:
        current = current.next
        next_node = current.next
        place = place + 1

        if place + 1 == position:
            current.next = Node(data)
            current.next.next = next_node

    return head
