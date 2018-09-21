def reverse_print(head):
    if head is None:
        return
    else:
        reversePrint(head.next)
    print(head.data)