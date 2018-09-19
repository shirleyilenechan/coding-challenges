def middle_node(self, head):
    node_lst = []

    current = head

    while current is not None:
        node_lst.append(current)
        current = current.next

    middle = len(node_lst) // 2

    return node_lst[middle]
