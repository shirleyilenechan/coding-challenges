def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next
